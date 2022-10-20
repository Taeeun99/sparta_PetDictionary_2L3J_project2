from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'input'

urlpatterns = [
    
    path('main/', views.main, name='main'),
    path('input/', views.input, name='input'),
    path('output/<int:id>/', views.output, name='output'),
    path('wrong/<int:id>/', views.if_wrong, name='wrong'),
    path('graph/', views.graph, name='graph'),

]

