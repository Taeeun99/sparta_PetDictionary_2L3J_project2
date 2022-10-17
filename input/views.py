from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    return render(request, 'main.html')
    

def input(request):
    return render(request, 'input.html')

def output(request):
    return render(request, 'output.html')

def if_worng(request):
    return render(request, 'if_worng.html')

def graph(request):
    return render(request, 'accuracy_graph.html')