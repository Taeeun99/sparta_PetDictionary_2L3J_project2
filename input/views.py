from django.shortcuts import render
from django.http import HttpResponse
from . import search, inference
from .models import InputModel, ResearchModel


# Create your views here.

def main(request):
    return render(request, 'main.html')
    

def input(request):
    if request.method == 'GET':
        return render(request, 'input.html')
    
    elif request.method == 'POST':
        '''
        여기에 inference.py 함수 돌리기
        
        InputModel.objects.create
        '''
    return redirect('/output')


def output(request):
    if request.method == 'GET':
        '''
        InputModel id로 받아오기
        '''        
        
        return render(request, 'output.html', {'img_data':img_data, 'species':species, 'breed':breed, 'search_link':search_link})
    
    elif


def if_wrong(request):
    
    
    if request.method == 'POST':
        search_data = request.POST.get("search")
        context=search.serch_cat(search_data)

        return render(request, 'if_wrong.html', context)

    elif request.method == 'GET':
        return render(request, 'if_wrong.html')

  



def graph(request):
    if request.method == 'GET':
        ResearchModel.objects.create(correct=True)
        return render(request, 'accuracy_graph.html',{'data':30})
