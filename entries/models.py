from django.db import models

from schools.models import School
from students.models import Student


class Entry(models.Model):
    id = models.AutoField('id', primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)

    entered_at = models.DateTimeField('Entered at')

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    class Meta:
        ordering = ['id']
        db_table = 'entries'

    def __str__(self):
        return self.id
