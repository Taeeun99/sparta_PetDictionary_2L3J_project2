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
    # 머신러닝 실행 
    # 결과값(정답라벨) DB에 저장 
    
    if request.method == 'POST': # 1번째 POST
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

    elif request.method == 'POST': # 2번째 POST

        if request.POST.get('correct') == 'yes': # 정확도 설문 답변이 value="yes"라면 
            my_correct = ResearchModel.objects.create(correct=True)
            print(my_correct.get('correct'))     #필드값 생성 추가
            return redirect('/graph')

        elif request.POST.get('correct') == 'no':
            my_correct =ResearchModel.objects.create(correct=False)
            print(my_correct.get('correct'))
            return redirect('/worng')
        
        else:
            return redirect('/graph')


def if_worng(request):
    return render(request, 'if_worng.html')


def graph(request):
    return render(request, 'accuracy_graph.html')