#-*- coding:utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import torch
from PIL import Image
import base64

model = torch.hub.load('ultralytics/yolov5', 'custom', path='models_train/best.pt', force_reload=True)
img = Image.open('test.jpg')
# img = cv2.imread('test.jpg') # batch of images

results3 = model(img)

# results3.save()
results3.ims  # array of original images (as np array) passed to model for inference 원본 이미지(np 배열) 추론모델로 보내기
results3.render()  # updates results.imgs with boxes and labels  이미지에 박스와 라벨 붙이기
for img in results3.ims:  # 'JpegImageFile' -> bytes-like object
    buffered = io.BytesIO()
    img_base64 = Image.fromarray(img)
    img_base64.save(buffered, format="JPEG")
    encoded_img_data = base64.b64encode(buffered.getvalue()).decode(
        'utf-8')  # base64 encoded image with results


#사물인식 돌린 결과를 numpy 계열로 바꿈
result = results3.pandas().xyxy[0].to_numpy()
print(result)

species = result[0][6][:3]
breed = result[0][6][4:]

print(result[0][6])

print(f'검색하신 {species}는 {breed} 입니다.')

print(f'https://google.com/search?q={result[0][6]}')

# print(encoded_img_data)
