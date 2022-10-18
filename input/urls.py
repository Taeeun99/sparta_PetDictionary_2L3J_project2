from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('main/', views.main, name='main'),
    path('input/', views.input, name='input'),
    path('output/', views.output, name='output'),
    path('worng/', views.if_worng, name='worng'),
    path('graph/', views.graph, name='graph'),

]

