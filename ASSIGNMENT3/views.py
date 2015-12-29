from django.shortcuts import render,HttpResponseRedirect,render_to_response,RequestContext
from forms import *
from models import *
# Create your views here.


def addteacher(request):
    if request.method == 'POST':
        form = Teacher1(request.POST)
        if form.is_valid():
            a = Teacher(first_name=form.cleaned_data["first_name"],  last_name=form.cleaned_data["last_name"], office =form.cleaned_data["office"], details=form.cleaned_data["details"], phone=form.cleaned_data["phone"], email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/all-teachers/')
    else:
        form = Teacher1(initial= {'first_name':''})
        return render_to_response('add_teacher.html', {'form': form},  RequestContext(request))



def addstudent(request):
    if request.method == 'POST':
        form = Student1(request.POST)
        if form.is_valid():
            a = Student(first_name=form.cleaned_data["first_name"],  last_name=form.cleaned_data["last_name"], email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/all-students/')
    else:
        form = Student1(initial= {'first_name':''})
        return render_to_response('add_student.html', {'form': form},  RequestContext(request))



def addcourse(request):
    if request.method == 'POST':
        form = Course1(request.POST)
        if form.is_valid():
            a = Course(course_name=form.cleaned_data["cours_name"],  course_code=form.cleaned_data["course_code"], course_class=form.cleaned_data["course_class"]),
            a.save()
            return HttpResponseRedirect('/all-courses/')
    else:
        form = Student1(initial= {'first_name':''})
        return render_to_response('add_course.html', {'form': form},  RequestContext(request))



def listof_students(request):
    return render_to_response('listof_students.html', {'student_list': Student.objects.all()})

def listof_teachers(request):
    return render_to_response('listof_teachers.html', {'teacher_list': Teacher.objects.all()})

def listof_courses(request):
    return render_to_response('listof_courses.html', {'course_list': Course.objects.all()})