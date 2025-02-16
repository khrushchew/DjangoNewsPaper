from django.views import View
from django.shortcuts import render

from core.models.post import Post


class RetrieveNewsView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            post = Post.objects.get(pk=pk)
        except:
            pass
        return render(request, 'detail.html', {'post': post})
