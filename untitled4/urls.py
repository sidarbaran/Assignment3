"""untitled4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from ASSIGNMENT3 import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add_teacher/$',views.addteacher),
    url(r'^add_student/$',views.addstudent),
    url(r'^add_course/$',views.addcourse),
    url(r'^all-students/$',views.listof_students),
    url(r'^all-courses/$',views.listof_courses),
    url(r'^all-teachers/$',views.listof_teachers)
]
