from django.db import models  # Importing Django's models module to define model classes
from django.contrib.auth.models import User  # Importing the User model to create a relationship with the built-in User model

# Defining the Student model
class Student(models.Model):
    # Establishing a ForeignKey relationship to the User model (the teacher)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)  # Links each student to a teacher (using Django's built-in User model)
    
    # Defining fields for the student’s name, subject, and marks
    name = models.CharField(max_length=100)  # A field to store the student's name, with a maximum length of 100 characters
    subject = models.CharField(max_length=100)  # A field to store the subject of the student, with a maximum length of 100 characters
    marks = models.IntegerField()  # A field to store the student's marks (integer value)

    # Method to return a human-readable string representation of the Student object
    def __str__(self):
        # The string representation returns the student's name and subject for easier identification
        return f'{self.name} - {self.subject}'
