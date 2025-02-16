from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User

from core.models.post import Post
from core.models.comment import Comment


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    
    def update_rating(self):
        post_rating = Post.objects.filter(author=self, category='A').aggregate(total=Sum('rating'))
        comments_rating = Comment.objects.filter(user=self.user).aggregate(total=Sum('rating'))
        posts_comments_rating = Post.objects.filter(author=self).comments.aggregate(total=Sum('rating'))
        self.rating = post_rating['total'] * 3 + comments_rating['total'] + posts_comments_rating['total']
        self.save()
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = "author"
        verbose_name_plural = 'Авторы'
        verbose_name = 'Автор'
        ordering = ['-rating']
