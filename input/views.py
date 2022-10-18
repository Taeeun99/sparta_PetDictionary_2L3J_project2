from django.shortcuts import render
from django.http import HttpResponse
from . import search




# Create your views here.

def main(request):
    return render(request, 'main.html')
    

def input(request):
    return render(request, 'input.html')

def output(request):
    return render(request, 'output.html')

def if_wrong(request):
    search.serch_cat('스핑크스고양이')

    return render(request, 'if_wrong.html')

def graph(request):
    return render(request, 'accuracy_graph.html', {'data':10})