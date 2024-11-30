# -*- coding: utf-8 -*-
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import StudentForm
from .models import Student


class StudentList(ListView): 
    model = Student

class StudentDetail(DetailView): 
    model = Student

class StudentCreate(SuccessMessageMixin, CreateView): 
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student_list')
    success_message = "Aluno criado com sucesso!"

class StudentUpdate(SuccessMessageMixin, UpdateView): 
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student_list')
    success_message = "Aluno atualizado com sucesso!"

class StudentDelete(SuccessMessageMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')
    success_message = "Aluno excluído com sucesso!"

