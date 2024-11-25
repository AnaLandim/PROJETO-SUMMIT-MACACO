from django.db import models


class Student(models.Model):
    id = models.AutoField('id', primary_key=True)
    name = models.CharField('Name', max_length=100)
    age = models.IntegerField('Age')
    phone = models.CharField('Phone', max_length=15)
    email = models.EmailField('Email', max_length=100)

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    class Meta:
        ordering = ['name']
        db_table = 'students'

    def __str__(self):
        return self.name
