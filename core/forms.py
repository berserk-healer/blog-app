from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {'content': SummernoteWidget(),}


class PostEditForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {'content': SummernoteWidget()}


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['body']
        labels = {'body': '',}
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 
                                          'placeholder': 'Join the discussion and leave a comment!',
                                          'rows': '3',
                                          'style': 'resize: none'})
        }