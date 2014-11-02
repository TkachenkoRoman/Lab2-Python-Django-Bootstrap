from django.shortcuts import render
from guitar_app import tables, models
from django_tables2   import RequestConfig
from django.http import HttpResponse, HttpResponseRedirect
import forms
import sql_scripts
from django.db import connection
from django.forms.models import modelformset_factory

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
            if action == 'statistics':
                return HttpResponseRedirect('/statistics/')
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


def history_action(request):
    if request.method == 'POST':
        VarFormSet = modelformset_factory(models.Variables, form=forms.VariablesForm, extra=0)
        formset = VarFormSet(request.POST)
        for form in formset:
            form.save()
    return HttpResponseRedirect('/')

def history(request):
    VarFormSet = modelformset_factory(models.Variables, form=forms.VariablesForm, extra=0)
    formset = VarFormSet()
    table = tables.HistoryTable(models.History.objects.all())
    RequestConfig(request).configure(table)

    return render(request, 'guitar_app/history.html', {'table': table, 'formset': formset})

def statistics(request):
    table = tables.StatisticsTable(sql_scripts.get_statistics())
    RequestConfig(request).configure(table)
    return render(request, "guitar_app/statistics.html", {"table": table})