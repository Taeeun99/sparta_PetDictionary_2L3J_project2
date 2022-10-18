from django.shortcuts import render, redirect

# Create your views here.
def output(request): # 이미지 분석 라벨을 키워드로 구글 검색

    if request.method = 'GET':
        keyword = Input.objects.get('pet') # DB에서 이미지 분석 라벨값 호출
        search_link = "https://www.google.com/search?q="+keyword # 구글 검색 url
        return render(request, 'search.html', {'search_link':search_link})

    elif request.method = 'POST': # 설문 결과에 따라 redirect (Y 설문결과 페이지, N 재검색 페이지)
        text = request.POST.get("test")
        img = request.FILES.get("imgfile")
        print(img, text)
        my_search = InputModel.objects.create(imgfile=img)  # 이미지 저장
        # my_search.save()

        if request.POST.get('correct') == 'yes': # 정확도 설문 답변이 yes라면 -> html에서 value="yes" 지정 필요
            Research.create(correct = True)
            return redirect('/') # 설문 결과 페이지로 연결

        elif request.POST.get('correct') == 'no': # 정확도 설문 답변이 no라면
            Research.objects.create(correct = False) # 
            return redirect('/') # 재검색 페이지로 연결
        




