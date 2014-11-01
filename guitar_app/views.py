from django.shortcuts import render
from guitar_app import tables, models
from django_tables2   import RequestConfig
from django.http import HttpResponse, HttpResponseRedirect
import forms
import sql_scripts
from django.db import connection
# Create your views here.

def index(request):
    table = tables.GuitarTable(models.Guitar.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'guitar_app/index.html', {'table': table})

def action(request):
    if request.method == 'POST':
        action = request.POST.get('action', False)
        if action:
            pks = request.POST.getlist("selection")
            #selected_objects = models.Guitar.objects.filter(pk__in=pks)
            if action == 'delete':
                models.Guitar.objects.filter(pk__in=pks).delete()
            if action == 'history':
                return HttpResponseRedirect('/history/')
            if action == 'load':
                return HttpResponseRedirect('/load_data_from_file/')
        return HttpResponseRedirect('/')
    return HttpResponse('no POST in action view')

def add(request):
    if request.method == 'POST':
        form = forms.GuitarAddForm(request.POST)
        if form.is_valid():
            guitar = form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Form is not valid')
    else:
        form = forms.GuitarAddForm()
    return render(request,'guitar_app/add.html', {'form': form})

def guitar_detail(request, pk):
    if request.method == 'POST':
        form = forms.GuitarAddForm(request.POST)
        if form.is_valid():
            guitar = models.Guitar.objects.get(pk=pk)
            t = forms.GuitarAddForm(request.POST, instance=guitar)
            t.save()
            return HttpResponseRedirect('/')
    else:
        form = forms.GuitarAddForm(instance=models.Guitar.objects.get(pk=pk))
        return render(request, 'guitar_app/guitar_detail.html', {'form': form, 'pk': pk})

def load_data_view(request):
    sql_scripts.load_data_from_files()
    return HttpResponseRedirect('/')



def history(request):
    insert = sql_scripts.get_trigger_insert_value()
    if request.method == 'POST':
        if 'insert' not in request.POST:
            sql_scripts.insert = ""
            sql_scripts.disable_history_insert(True)
        else:
            sql_scripts.insert = "checked"
            sql_scripts.disable_history_insert(False)
        return HttpResponseRedirect('/')
    else:
        table = tables.HistoryTable(models.History.objects.all())
        RequestConfig(request).configure(table)
    return render(request, 'guitar_app/history.html', {'table': table, 'insert': insert,\
                                                       'update': sql_scripts.update, 'delete': sql_scripts.delete})