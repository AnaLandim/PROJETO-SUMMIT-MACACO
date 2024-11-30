# -*- coding: utf-8 -*-
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import EntryForm
from .models import Entry


class EntryList(ListView): 
    model = Entry

class EntryDetail(DetailView): 
    model = Entry

class EntryCreate(SuccessMessageMixin, CreateView): 
    model = Entry
    form_class = EntryForm
    success_url = reverse_lazy('entry_list')
    success_message = "Entrada criada com sucesso!"

class EntryUpdate(SuccessMessageMixin, UpdateView): 
    model = Entry
    form_class = EntryForm
    success_url = reverse_lazy('entry_list')
    success_message = "Entrada atualizada com sucesso!"

class EntryDelete(SuccessMessageMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy('entry_list')
    success_message = "Entrada excluída com sucesso!"
