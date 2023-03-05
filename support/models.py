from django.db import models

class Contacts(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    desctiprion = models.TextField(max_length=1000)
    phone = models.CharField(max_length=20)
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name