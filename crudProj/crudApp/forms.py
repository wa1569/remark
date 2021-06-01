from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        #post 모델
        model = Post
        #post 모델 중에서 title, writer, body 값을 입력받음
        fields = ['title', 'writer', 'body']