from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed


class Student(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed


class Admin(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed
