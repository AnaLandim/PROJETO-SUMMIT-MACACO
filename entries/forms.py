# forms.py
from django import forms

from students.models import Student

from .models import Entry


class EntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)
        self.fields["student"] = forms.ModelChoiceField(
            queryset=Student.objects.all(),
            widget=forms.Select(attrs={"class": "form-control col-md-6"}),
            empty_label="Selecione um Aluno"
        )
        self.fields["entered_at"].widget = forms.DateTimeInput(
            attrs={"class": "form-control col-md-6", "type": "datetime-local", "step": 1},
            format='%d/%m/%Y %H:%M'
        )

    class Meta:
        model = Entry
        fields = ("student", "entered_at")