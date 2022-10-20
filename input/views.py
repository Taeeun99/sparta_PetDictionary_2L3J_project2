from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import search, inference
from .models import InputModel, Image
from googletrans import Translator


# Create your views here.

def main(request):
    return render(request, 'main.html')
    

def input(request):
    if request.method == 'GET':
        return render(request, 'input.html')
    
    elif request.method == 'POST':
        img = request.FILES.get("imgfile")
        if img: 
            giveimage = Image.objects.create(imgfile=img)

            
            img_loc = giveimage.imgfile
            media_loc = 'media/' + str(img_loc)
            output_data = inference.inference(media_loc)

            if output_data==1:
                return render(request, 'input.html',{'error' : '이미지 인식 오류, 이미지를 다시 등록해주세요'})

        #모델 저장
            my_search = InputModel()
            my_search.img_data = output_data['img_data']
            my_search.species = output_data['species']
            my_search.breed = output_data['breed']
            my_search.search_link = output_data['search_link']
            my_search.save()
       
            return redirect(f'/output/{my_search.id}')
        else:
            return render(request, 'input.html',{'error' : '이미지가 등록되지 않았습니다'})



def output(request, id):
    my_pet = InputModel.objects.get(id=id)

    if request.method == 'GET':
        
        
        species = my_pet.species
        breed = my_pet.breed
        search_link = my_pet.search_link
        img_data = my_pet.img_data
       
        trans = Translator() 
        result = trans.translate(species, src='en', dest='ko')
        species_ko = result.text

        search_data = f'{breed}'
        context = search.serch_cat(search_data) 
        if context['none']== True:
            search_data = f'{breed} {species}'
            context = search.serch_cat(search_data)  
       
        info = {
            'species_ko':species_ko,
            'breed':breed,
            'search_link':search_link,
            'img_data':img_data,
            'context':context,
            'id':id,
        }

        return render(request, 'output.html', info)

    elif request.method == 'POST':
        id=id
        result = request.POST.get('result') # 검색 정확도 설문 결과
        if result == 'yes':
             my_pet.correct = True
             my_pet.save()
             return redirect('/graph')
        
        elif result == 'no':
            my_pet.correct = False
            my_pet.save()
            return redirect(f'/wrong/{id}') 


def if_wrong(request, id):
    
    if request.method == 'POST':
        search_data = request.POST.get("search")
        context=search.serch_cat(search_data)

        my_pet = InputModel.objects.get(id=id)
       
        my_pet.pet_result = search_data   # 재검색 시 사용한 keyword
        my_pet.save()   # 재검색 결과를 DB에 저장

        return render(request, 'if_wrong.html', context)

    elif request.method == 'GET':
        return render(request, 'if_wrong.html', {'id':id})

  



def graph(request):
    if request.method == 'GET':

        yes = InputModel.objects.filter(correct=1).count()
        total = InputModel.objects.all().count()
        if total == 0 :
            percent = 0
        else:
            percent = int((yes/total)*100)
        
        return render(request, 'accuracy_graph.html',{'data':percent})

