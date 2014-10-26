from django.shortcuts import render
from guitar_app import tables, models
from django_tables2   import RequestConfig
from django.http import HttpResponse, HttpResponseRedirect
import forms
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
    if request.method == 'GET':
        return HttpResponse('GET guitar_detail')
    else:
        form = forms.GuitarAddForm(instance=models.Guitar.objects.get(pk=pk))
        return render(request, 'guitar_app/guitar_detail.html', {'form': form, 'pk': pk})