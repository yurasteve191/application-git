from django.db import models
import os

class News(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200, null=True, blank=True)
    short_description = models.TextField(verbose_name='Короткий опис', null=True, blank=True)
    full_description = models.TextField(verbose_name='Повний опис', null=True, blank=True)
    image = models.ImageField(upload_to='news/%Y/%m/%d/', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Новини'

    def delete(self, *args, **kwargs):
        os.remove(self.image.path)
        super(TopNews, self).delete(*args, **kwargs)

class Actions(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200, null=True, blank=True)
    short_description = models.TextField(verbose_name='Короткий опис', null=True, blank=True)
    full_description = models.TextField(verbose_name='Повний опис', null=True, blank=True)
    image = models.ImageField(upload_to='action/%Y/%m/%d/', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Події'

    def delete(self, *args, **kwargs):
        os.remove(self.image.path)
        super(Actions, self).delete(*args, **kwargs)

class Music(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200, null=True, blank=True)
    short_description = models.TextField(verbose_name='Короткий опис', null=True, blank=True)
    full_description = models.TextField(verbose_name='Повний опис', null=True, blank=True)
    image = models.ImageField(upload_to='music/%Y/%m/%d/', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Музика'

    def delete(self, *args, **kwargs):
        os.remove(self.image.path)
        super(Music, self).delete(*args, **kwargs)

class TopNews(models.Model):
    short_description = models.TextField(verbose_name='Короткий опис', max_length=500)
    image = models.ImageField(upload_to='topNews/%Y/%m/%d/')
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Новини - слайди'
    
    def delete(self, *args, **kwargs):
        os.remove(self.image.path)
        super(TopNews, self).delete(*args, **kwargs)