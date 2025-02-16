from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    post = models.ForeignKey('post', on_delete=models.CASCADE, related_name='comments')
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
    
    class Meta:
        db_table = "comment"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['-time_of_creating']
