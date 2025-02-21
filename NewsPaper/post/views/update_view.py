from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.forms.models import model_to_dict

from post.forms.create_form import CreatePostForm
from core.models.post import Post
from core.models.author import Author


class UpdatePostView(View):
    form_class = CreatePostForm
    type_of_post = None

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        model = Post.objects.get(pk=pk)
        form = self.form_class(model_to_dict(model))
        return render(request, 'crud/update.html', {'form': form, 'pk': pk, 'type_of_post': self.type_of_post})
    
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        model = Post.objects.get(pk=pk)
        form = self.form_class(data=request.POST, instance=model)
        if form.is_valid():
            form.save(author=Author.objects.get(pk=1), type_of_post=self.type_of_post)
            return HttpResponseRedirect('/news/') if self.type_of_post == 'N' else HttpResponseRedirect('/articles/')
        else:
            return render(request, 'crud/update.html', {'form': form})
