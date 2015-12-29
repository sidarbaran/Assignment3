
from django import forms


class Teacher1(forms.Form):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    office=forms.CharField(max_length=30)
    details=forms.CharField(max_length=30)
    phone=forms.IntegerField()
    email=forms.EmailField()


class Student1(forms.Form):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    email=forms.EmailField()


class Course1(forms.Form):
    name=forms.CharField(max_length=30)
    code=forms.CharField(max_length=30)
    classroom=forms.CharField(max_length=30)
    times=forms.TimeField()

