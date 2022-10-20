import torch
from PIL import Image
import base64
import io
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView






def inference(img):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='models_train/best.pt', force_reload=True)  # 커스텀 학습 모델 사용
    img = Image.open(img)
    

    results = model(img, size=640)  # inference 추론
    result = results.pandas().xyxy[0].to_numpy()  # 종-품명 추출하기 위해 numpy array
    if result == []:
        keyword = result[0][6]
        search_link = "https://www.google.com/search?q="+keyword
        species = keyword[:3]  # 종
        breed = keyword[4:]  # 품명
        results.ims  # array of original images (as np array) passed to model for inference 원본 이미지(np 배열) 추론모델로 보내기
        results.render()  # updates results.imgs with boxes and labels  이미지에 박스와 라벨 붙이기
        for img in results.ims:  # 'JpegImageFile' -> bytes-like object
            buffered = io.BytesIO()
            img_base64 = Image.fromarray(img)
            img_base64.save(buffered, format="JPEG")
            encoded_img_data = base64.b64encode(buffered.getvalue()).decode(
                'utf-8')  # base64 encoded image with results
            
        
        outputs_data = {
            'img_data' : encoded_img_data,
            'species' : species,
            'breed' : breed,
            'search_link' : search_link,
            }
        
        return outputs_data
    else:
        return 1

    
