from django.db import models

class Contacts(models.Model):
    name = models.CharField(verbose_name="Ім'я", max_length=255)
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Контакти'

class Feedback(models.Model):
    name = models.CharField(verbose_name="Ім'я", max_length=255)
    desctiprion = models.TextField(verbose_name='Опис', max_length=1000)
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    rate = models.IntegerField(verbose_name='Оцінка', )
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Відгуки'


class RentingShelves(models.Model):
    name = models.CharField(verbose_name="Ім'я", max_length=255)
    desctiprion = models.TextField(verbose_name='Опис', max_length=1000)
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    rate = models.IntegerField(verbose_name='Оцінка', )
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Оренда стелажів'

class RentingCanvas(models.Model):
    name = models.CharField(verbose_name="Ім'я", max_length=255)
    desctiprion = models.TextField(verbose_name='Опис', max_length=1000)
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    rate = models.IntegerField(verbose_name='Оцінка', )
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Оренда полотна'
    
