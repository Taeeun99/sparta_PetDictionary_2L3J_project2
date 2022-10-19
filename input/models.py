from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

# 이미지 파일 업로드 모델
class InputModel(models.Model):
    # 이미지 파일 업로드
    imgfile = models.ImageField(null=False, upload_to="input/", blank=False)
    # 품종이름
    pet = models.CharField(max_length=20)
    
    img_data = models.CharField('')
    # 사물인식 파일(base64 인코딩)
    species = models.CharField('')
    # 종
    breed = models.CharField('')
    # 품종
    search_link = models.CharField('')
    # 서치링크
   

class ResearchModel(models.Model):
    # 정확도

    correct = models.BooleanField(default=False)
    # 검색된 품종 이름
    pet_result = models.CharField(max_length=20)
    # 품종이름이 다를때
    pet_def = models.CharField(max_length=20)


    
