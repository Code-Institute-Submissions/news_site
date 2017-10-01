from django import forms
from .models import Article

class ArticlePostForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'intro', 'content', 'image', 'status', 'category', 'is_the_chosen_one')
