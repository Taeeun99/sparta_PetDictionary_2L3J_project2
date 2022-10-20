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
        #모델 저장
        my_search.img_data = output_data['img_data']
        my_search.species = output_data['species']
        my_search.breed = output_data['breed']
        my_search.search_link = output_data['search_link']
        my_search.save()
       
    return render(request, 'output.html', output_data) 


def output(request):
    if request.method == 'GET':
        '''
        InputModel id로 받아오기
        '''        
        #{'img_data':img_data, 'species':species, 'breed':breed, 'search_link':search_link}
        return redirect('/output')
    
    


def if_wrong(request):
    
    
    if request.method == 'POST':
        search_data = request.POST.get("search")
        context=search.serch_cat(search_data)
        return render(request, 'if_wrong.html', context)

    elif request.method == 'GET':
        return render(request, 'if_wrong.html')

  



def graph(request):
    if request.method == 'GET':

        yes = ResearchModel.objects.filter(correct=1).count()
        total = ResearchModel.objects.all().count()
        percent = int((yes/total)*100)

        print(percent)

    
        return render(request, 'accuracy_graph.html',{'data':percent})

