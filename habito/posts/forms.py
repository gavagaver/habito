from django.forms import ModelForm
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'habit', 'image']
        labels = {
            'text': 'Введите текст поста:',

        }
        help_texts = {

        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
