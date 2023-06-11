from django import forms
from app.models import *



class UserForm(forms.ModelForm):
    class Meta():
        model=User
        fields=['username','email','password']
        labels={'username':"Mobile number"}
        widgets={'password':forms.PasswordInput()}


class StudentForm(forms.ModelForm):
    class Meta():
        model=StudentData
        fields=['cname','YOP','HighestQualification','address']

class StudentRatingForm(forms.ModelForm):
    class Meta():
        model=StudentRating
        fields=["cname","coding","theory","comminication"]

