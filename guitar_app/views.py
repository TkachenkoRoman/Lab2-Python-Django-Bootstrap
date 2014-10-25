from django.shortcuts import render
from guitar_app import tables, models
from django_tables2   import RequestConfig
from django.http import HttpResponse
import forms
# Create your views here.

def index(request):
    table = tables.GuitarTable(models.Guitar.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'guitar_app/index.html', {'table': table})

def action(request):
    return HttpResponse('action')

def add(request):
    form = forms.GuitarAddForm()
    return render(request,'guitar_app/add.html', {'form': form})