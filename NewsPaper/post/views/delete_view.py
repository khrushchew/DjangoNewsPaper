from django.views import View
from django.http import HttpResponseRedirect

from core.models.post import Post


class DeletePostView(View):
    type_of_post = None

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        post.delete()
        return HttpResponseRedirect('/news/') if self.type_of_post == 'N' else HttpResponseRedirect('/articles/')
