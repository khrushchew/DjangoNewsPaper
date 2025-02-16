from django.views import View
from django.shortcuts import render
from django.core.paginator import Paginator

from core.models.post import Post

from news.filters.news_filter import NewsFilter


class ListNewsView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        posts_filter = NewsFilter(request.GET, posts)
        paginator = Paginator(posts_filter.qs, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'default.html', {'page_obj': page_obj, 'posts_filter': posts_filter})
