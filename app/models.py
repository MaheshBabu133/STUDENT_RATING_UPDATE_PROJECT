from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Year(models.Model):
    year=models.IntegerField()
    def __str__(self):
        return str(self.year)

class Course(models.Model):
    cname=models.CharField(max_length=100)
    def __str__(self):
        return self.cname

class Qualification(models.Model):
    HighestQualification=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.HighestQualification

class StudentData(models.Model):
    Name=models.CharField(max_length=50,default="maha")
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    cname=models.ForeignKey(Course,on_delete=models.CASCADE)
    YOP=models.ForeignKey(Year,on_delete=models.CASCADE)
    HighestQualification=models.ForeignKey(Qualification,on_delete=models.Model)
    address=models.TextField()
    def __str__(self):
        return self.Name
    


class Theory(models.Model):
    theory=models.CharField(max_length=100)
    def __str__(self):
        return self.theory

class Comunication(models.Model):
    comminication=models.CharField(max_length=100)
    def __str__(self):
        return self.comminication


class Coding(models.Model):
    coding=models.CharField(max_length=100)
    def __str__(self):
        return self.coding


class StudentRating(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    cname=models.CharField(max_length=100)
    coding=models.CharField(max_length=100)
    theory=models.CharField(max_length=100)
    comminication=models.CharField(max_length=100)
    