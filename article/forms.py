from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        widgets = {

            # <input type="text" class="form-control" placeholder="Username" aria-describedby="sizing-addon1">


            'content': forms.Textarea(attrs={'data-provide' : 'markdown', 'placeholder' : 'Write your comment here'}),
        }