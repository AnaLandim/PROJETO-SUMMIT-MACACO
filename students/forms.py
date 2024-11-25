# -*- coding: utf-8 -*-
from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['age'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['phone'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }
        self.fields['email'].widget.attrs = {
            'class': 'form-control col-md-6'
        }

    class Meta:
        model = Student
        fields = ('name', 'age', 'phone', 'email')