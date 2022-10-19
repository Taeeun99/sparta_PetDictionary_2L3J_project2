from django.shortcuts import render, redirect
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
        img = request.FILES.get("imgfile")
        my_search = InputModel.objects.create(imgfile=img)
        my_search.save()
       
        img_loc = my_search.imgfile
        media_loc = 'media/' + str(img_loc)

        output_data = inference.inference(media_loc)
        
        print(output_data['species'], output_data['breed'])

    return redirect(f'/output/{my_search.id}')



def output(request, id):
    
    if request.method == 'GET':
        
        my_pet = InputModel.objects.get(id=id)
        
        species = my_pet.species
        breed = my_pet.breed
        search_link = my_pet.search_link
        img_data = my_pet.img_data

        search_data = f'{breed} {species}'    
        context = search.serch_cat(search_data)        
        
        info = {
            'species':species,
            'breed':breed,
            'search_link':search_link,
            'img_data':img_data,
            'context':context,
            'id':id,
        }
        return render(request, 'output.html', info)

    elif request.method == 'POST':
        
        result = request.POST.get('result') # 검색 정확도 설문 결과
        if result == 'yes':
             ResearchModel.objects.create(correct=True)
             return redirect('/graph')
        
        elif result == 'no':
             ResearchModel.objects.create(correct=False)
             return redirect('/wrong') 



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
