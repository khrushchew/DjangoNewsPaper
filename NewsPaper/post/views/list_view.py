from django.views import View
from django.shortcuts import render
from django.core.paginator import Paginator

from core.models.post import Post

from post.filters.post_filter import PostFilter


class ListPostView(View):
    type_of_post = None

    def get(self, request, *args, **kwargs):
        if request.user:
            posts = Post.objects.filter(author__user=request.user, type_of_post=self.type_of_post)
        else:
            posts = Post.objects.filter(type_of_post=self.type_of_post)
        posts_filter = PostFilter(request.GET, posts)
        paginator = Paginator(posts_filter.qs, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'default.html', {'page_obj': page_obj, 'posts_filter': posts_filter})
