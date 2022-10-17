from django.shortcuts import render
from django.http import HttpResponse
from .models import InputModel
import os
# Create your views here.

def main(request):
    return render(request, 'main.html')
    

def input(request):
    
    return render(request, 'input.html')


def output(request):
    text = request.POST.get("test")
    img = request.FILES.get("imgfile")
    print(img, text)
    my_search = InputModel.objects.create(imgfile=img)  # 이미지 저장
    my_search.save()
    return render(request, 'output.html')


def if_worng(request):
    return render(request, 'if_worng.html')

def graph(request):
    return render(request, 'accuracy_graph.html')