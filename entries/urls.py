# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('entries', views.EntryList.as_view(), name='entry_list'),
    path('entries/view/<int:pk>', views.EntryDetail.as_view(), name='entry_view'),
    path('entries/new', views.EntryCreate.as_view(), name='entry_new'),
    path('entries/edit/<int:pk>', views.EntryUpdate.as_view(), name='entry_edit'),
    path('entries/delete/<int:pk>', views.EntryDelete.as_view(), name='entry_delete'),
]