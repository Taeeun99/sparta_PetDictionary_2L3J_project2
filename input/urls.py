from django.urls import path
from input import views

urlpatterns = [
    path('output/', views.output, name="output"),
]
