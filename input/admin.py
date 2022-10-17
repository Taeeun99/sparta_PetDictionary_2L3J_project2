from django.contrib import admin
from .models import InputModel
from .models import ResearchModel
# Register your models here.

# 나의 InputModel을 Admin에 추가 해 줍니다
admin.site.register(InputModel)