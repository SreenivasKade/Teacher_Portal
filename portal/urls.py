# Importing the necessary functions from Django
from django.urls import path  # Importing 'path' to define URL patterns
from . import views  # Importing views from the current app (portal)

# Defining the URL patterns for the "portal" app
# The 'app_name' variable is used to provide a namespace for the URLs, making it easier to refer to them in templates
app_name = 'portal'

# URL patterns list
urlpatterns = [
    # Login URL: This is the page where the teacher will log in
    # The URL '/login/' maps to the 'teacher_login' view in the views.py file
    path('login/', views.teacher_login, name='login'),

    # Home URL: This page serves as the home page for the teacher (with student listings)
    # The URL '/home/' maps to the 'teacher_home' view in the views.py file
    path('home/', views.teacher_home, name='teacher_home'),

    # Add Student URL: This page provides functionality to add a new student
    # The URL '/add_student/' maps to the 'add_student' view in the views.py file
    path('add_student/', views.add_student, name='add_student'),

    # Edit Student URL: This page allows the teacher to edit a specific student's details
    # The URL '/edit_student/<int:student_id>/' expects a student ID as an integer parameter
    # It maps to the 'update_student' view in the views.py file, and the student ID is passed to it
    path('edit_student/<int:student_id>/', views.update_student, name='edit_student'),

    # Delete Student URL: This page allows the teacher to delete a specific student's details
    # The URL '/delete_student/<int:student_id>/' expects a student ID as an integer parameter
    # It maps to the 'delete_student' view in the views.py file, and the student ID is passed to it
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),

    # Logout URL: This page handles the teacher's logout action
    # The URL '/logout/' maps to the 'teacher_logout' view in the views.py file
    path('logout/', views.teacher_logout, name='logout'),
]
