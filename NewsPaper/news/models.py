from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    
    # def update_rating(self):
    #     post_rating = Post.objects.filter(author=self).aggregate(pr=Coalesce(Sum('rating'), 0))
    #     comments_rating = Comment.objects.filter(user=self.user).aggregate(cr=Coalesce(Sum('rating'), 0))
    #     posts_comments_rating = Comment.objects.filter(author=self).aggregate(pcr=Coalesce(Sum('rating'), 0))
    #     self.rating = post_rating * 3 + comments_rating + posts_comments_rating
    #     self.save()
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Авторы'
        verbose_name = 'Автор'
        ordering = ['rating']
        

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)


class Post(models.Model):
    news = 'NE'
    articles = 'AR'
    
    POSITIONS = [
        (news, "Новость"),
        (articles, "Статья"),
    ]
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    type_of_post = models.CharField(max_length=2, choices=POSITIONS, default=news)
    time_of_creating = models.DateTimeField(auto_now_add=True)
    
    category = models.ManyToManyField(Category, through='PostCategory')
    
    title = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    
    def like(self):
        self.rating += 1
        self.save()
    
    def dislike(self):
        self.rating -= 1
        self.save()
        
    def preview(self):
        return f"{self.text[:124]}..."


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    text = models.CharField(max_length=500)
    time_of_creating = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    
    def like(self):
        self.rating += 1
        self.save()
        
    def dislike(self):
        self.rating -= 1
        self.save()