from django.shortcuts import render
from django.http import HttpResponse
from . import search
from .models import InputModel, ResearchModel


# Create your views here.

def main(request):
    return render(request, 'main.html')
    

def input(request):
    
    return render(request, 'input.html')


def output(request):


    img = request.FILES.get("imgfile")
    InputModel.objects.create(imgfile=img)  # 이미지 수신 후 저장
    # 머신러닝 실행 부분
    # 결과값(정답라벨)을 DB에 저장하는 부분
    
    if request.method == 'POST':
        # keyword = InputModel.objects.get('pet') # DB에서 이미지 분석 라벨값 호출
        keyword = 'cat-ddd' # DB에서 이미지 분석 라벨값 호출
        search_link = "https://www.google.com/search?q="+keyword # 구글 검색 url
        
        top_category = str(keyword.split('-')[:1])
        low_category = str(keyword.split('-')[1:])

        context = {
            'search_link':search_link,
            'top_category':top_category.strip("'" "[" "]"),
            'low_category':low_category.strip("'" "[" "]"),
        }
        
    
        return render(request, 'output.html', context)


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
