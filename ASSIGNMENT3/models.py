from django.db import models





class Teacher(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    office=models.CharField(max_length=30)
    details=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.EmailField()

class Student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()



class Course(models.Model):
    teacher= models.CharField(max_length=30)
    students=models.ManyToManyField(Student)
    name=models.CharField(max_length=30)
    code=models.CharField(max_length=30)
    classroom=models.CharField(max_length=30)
    times=models.TimeField()

