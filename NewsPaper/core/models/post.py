from django.db import models

from core.models.post_category import PostCategory


class Post(models.Model):
    POSITIONS = [
        ('N', "Новость"),
        ('A', "Статья"),
    ]
    
    author = models.ForeignKey('author', on_delete=models.CASCADE, verbose_name='Автор')
    
    type_of_post = models.CharField(max_length=1, choices=POSITIONS, default='N', verbose_name='Тип поста')
    time_of_creating = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    
    category = models.ManyToManyField('category', through=PostCategory, verbose_name='Категория')
    
    title = models.CharField(max_length=100, verbose_name='Название поста', null=False, blank=False)
    text = models.TextField(verbose_name='Содержание поста', null=False, blank=False)
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    
    def like(self):
        self.rating += 1
        self.save()
    
    def dislike(self):
        self.rating -= 1
        self.save()
        
    def preview(self):
        return f"{self.text[:124]}..."
    
    class Meta:
        db_table = 'post'
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'
        ordering = ['-time_of_creating']
        
    def __str__(self):
        return f"{self.title[:10]}..."
