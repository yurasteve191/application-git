from django.db import models
import os

class News(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    full_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='news/%Y/%m/%d/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        os.remove(self.image.path)
        super(TopNews, self).delete(*args, **kwargs)

class TopNews(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    image = models.ImageField(upload_to='topNews/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        os.remove(self.image.path)
        super(TopNews, self).delete(*args, **kwargs)