from django.forms import ModelForm
from django import forms

from core.models.post import Post
from core.models.category import Category


class CreatePostForm(ModelForm):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), label='Выберите категории', widget=forms.CheckboxSelectMultiple, required=True)
    title = forms.CharField(label='Название поста', widget=forms.Textarea, min_length=10, max_length=100)
    text = forms.CharField(label='Текст поста', widget=forms.Textarea, min_length=100)

    class Meta:
        model = Post
        fields = ('category', 'title', 'text')
    
    def save(self, commit=True, author=None, type_of_post=None):
        instance = super().save(commit=False)
        if author and type_of_post:
            instance.author = author
            instance.type_of_post = type_of_post
        instance.save()
        self.save_m2m()
        return instance
    