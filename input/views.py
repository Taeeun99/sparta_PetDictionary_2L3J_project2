from django.shortcuts import render, redirect
from django.http import HttpResponse
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


def if_worng(request):
    if request.method == 'GET': # 정확도 설문 답변이 no라면
        ResearchModel.objects.create(correct=False)
        return render(request, 'if_worng.html')
        
    elif request.method == 'POST': # 문자열 입력으로 재검색
        keyword = request.POST.get('keyword')
        search_link = "https://www.google.com/search?q="+keyword 
        return render(request, 'if_worng.html', {'search_link':search_link})


def graph(request):
    if request.method == 'GET':
        ResearchModel.objects.create(correct=True)
        return render(request, 'accuracy_graph.html')