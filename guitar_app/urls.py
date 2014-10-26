from django.conf.urls import patterns, include, url
from guitar_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^action/', views.action, name='action'),
    url(r'^add/', views.add, name='add'),
    url(r'^guitar_detail/(\d+)/', views.guitar_detail, name='guitar_detail')
)
