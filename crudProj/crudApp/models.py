from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    #제목
    title = models.CharField(max_length=200)
    #날짜
    pub_date = models.DateField('date published')
    #작성자
    #null 값 방지를 위해 default값 지정
    writer = models.CharField(null = False, max_length=15, default='닉네임을 입력해주세요.')
    #본문
    body = models.TextField()

    #제목 표시
    def __str__(self):
        return self.title