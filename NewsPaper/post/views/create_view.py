from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from post.forms.create_form import CreatePostForm

from core.models.author import Author


class CreatePostView(LoginRequiredMixin, View):
    form_class = CreatePostForm
    type_of_post = None

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(author=Author.objects.get(pk=1), type_of_post=self.type_of_post)
            return HttpResponseRedirect('/news/') if self.type_of_post == 'N' else HttpResponseRedirect('/articles/')
        else:
            return render(request, 'crud/create.html', {'form': form})
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'crud/create.html', {'form': form})
