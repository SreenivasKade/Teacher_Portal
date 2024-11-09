# Importing necessary modules from Django
from django import forms  # Importing Django's form module to define forms
from .models import Student  # Importing the Student model to create a form for it

# Defining a ModelForm for the Student model
class StudentForm(forms.ModelForm):
    # The 'Meta' class is used to configure the form’s model and fields
    class Meta:
        model = Student  # The form is based on the Student model
        fields = ['name', 'subject', 'marks']  # Only these fields will be included in the form

    # The fields 'name', 'subject', and 'marks' will automatically be generated from the Student model
    # You can add additional custom validation or widget configuration here if needed


# Defining a custom Form for handling teacher login
class LoginForm(forms.Form):
    # The login form does not tie to any model. It is a simple form to collect a username and password
    
    # Creating a form field for the username (string with a max length of 100 characters)
    username = forms.CharField(max_length=100)
    
    # Creating a form field for the password (password input field, so the input is hidden)
    password = forms.CharField(widget=forms.PasswordInput)
