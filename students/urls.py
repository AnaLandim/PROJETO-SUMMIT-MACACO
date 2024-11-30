# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('', views.StudentList.as_view(), name='student_list'),
    path('students/view/<int:pk>', views.StudentDetail.as_view(), name='student_view'),
    path('students/new', views.StudentCreate.as_view(), name='student_new'),
    path('students/edit/<int:pk>', views.StudentUpdate.as_view(), name='student_edit'),
    path('students/delete/<int:pk>', views.StudentDelete.as_view(), name='student_delete'),
]