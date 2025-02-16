from django.db import models


class PostCategory(models.Model):
    post = models.ForeignKey('post', on_delete=models.CASCADE)
    category = models.ForeignKey('category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'post_category'
