from django.contrib import admin
from .models import Question, Choice# .은 현재 있는 admin.py에 있는 models를 가져온다는 얘기
# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)