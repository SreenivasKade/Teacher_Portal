# Importing necessary modules from Django
from django.shortcuts import render, redirect  # render is used to render a template, redirect is used to redirect to another view
from django.contrib.auth import authenticate, login, logout  # For handling user authentication and login/logout
from django.http import JsonResponse  # For returning JSON responses
from .models import Student  # Importing the Student model to interact with the database
from .forms import StudentForm, LoginForm  # Importing forms for adding/updating students and handling login

# Teacher Login View
def teacher_login(request):
    if request.method == 'POST':  # If the form is submitted (POST request)
        form = LoginForm(request.POST)  # Initialize the form with the POST data
        if form.is_valid():  # Check if the form is valid
            username = form.cleaned_data['username']  # Get the username from cleaned data
            password = form.cleaned_data['password']  # Get the password from cleaned data
            user = authenticate(request, username=username, password=password)  # Authenticate the user

            if user is not None:  # If authentication is successful
                login(request, user)  # Log the user in
                return redirect('portal:teacher_home')  # Redirect to the home page
            else:
                # If the credentials are invalid, return the form with an error message
                return render(request, 'portal/login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = LoginForm()  # If it's a GET request, initialize an empty form
    return render(request, 'portal/login.html', {'form': form})  # Render the login page with the form

# Teacher Home View
def teacher_home(request):
    if not request.user.is_authenticated:  # Check if the user is authenticated
        return redirect('portal:login')  # If not authenticated, redirect to the login page
    
    students = Student.objects.filter(teacher=request.user)  # Get the students associated with the logged-in teacher
    return render(request, 'portal/home.html', {'students': students})  # Render the home page with the student list

# Add New Student View
def add_student(request):
    if request.method == 'POST':  # If the form is submitted (POST request)
        form = StudentForm(request.POST)  # Initialize the form with POST data
        if form.is_valid():  # Check if the form is valid
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            marks = form.cleaned_data['marks']

            # Check if a student with the same name and subject already exists for the current teacher
            existing_student = Student.objects.filter(teacher=request.user, name=name, subject=subject).first()
            if existing_student:  # If the student exists, update their marks
                existing_student.marks += marks  # Add the new marks to the existing ones
                existing_student.save()  # Save the updated student object
            else:
                # If the student doesn't exist, create a new student
                new_student = form.save(commit=False)  # Save the form without committing to the database
                new_student.teacher = request.user  # Assign the teacher (current user) to the new student
                new_student.save()  # Save the new student object to the database

            return redirect('portal:teacher_home')  # Redirect back to the teacher home page
    else:
        form = StudentForm()  # If it's a GET request, initialize an empty form
    return render(request, 'portal/add_student.html', {'form': form})  # Render the page to add a new student

# Update Student Details View
def update_student(request, student_id):
    student = Student.objects.get(id=student_id)  # Get the student by ID
    if request.method == 'POST':  # If the form is submitted (POST request)
        form = StudentForm(request.POST, instance=student)  # Initialize the form with the POST data and existing student instance
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the updated student details
            return redirect('portal:teacher_home')  # Redirect back to the home page
    else:
        form = StudentForm(instance=student)  # If it's a GET request, initialize the form with the current student data
    return render(request, 'portal/edit_student.html', {'form': form, 'student': student})  # Render the edit student page

# Delete Student View
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)  # Get the student by ID
    student.delete()  # Delete the student from the database
    return redirect('portal:teacher_home')  # Redirect back to the teacher home page

# Teacher Logout View
def teacher_logout(request):
    logout(request)  # Log the teacher out
    return redirect('portal:login')  # Redirect to the login page
