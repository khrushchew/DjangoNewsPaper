from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True, verbose_name='Категория')
    
    class Meta:
        db_table = "category"
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['category_name']

    def __str__(self):
        return f"{self.category_name}"
