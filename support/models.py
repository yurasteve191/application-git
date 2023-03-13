from django.db import models
from datetime import date

class Contacts(models.Model):
    name = models.CharField(verbose_name="Ім'я", max_length=255)
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    comentar = models.TextField(verbose_name='Коментар', max_length=1000, blank=True, null=True)
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
    comentar = models.TextField(verbose_name='Коментар', max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Відгуки'


class RentingShelves(models.Model):
    name = models.CharField(verbose_name="Ім'я", max_length=255)
    shelves_id = models.IntegerField(verbose_name='ID стелажа', default=0)
    desctiprion = models.TextField(verbose_name='Опис', max_length=1000)
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    comentar = models.TextField(verbose_name='Коментар', max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = '(Запити) Оренда стелажів'

class RentingCanvas(models.Model):
    name = models.CharField(verbose_name="Ім'я", max_length=255)
    canvas_id = models.IntegerField(verbose_name='ID полотна', default=0)
    desctiprion = models.TextField(verbose_name='Опис', max_length=1000)
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    comentar = models.TextField(verbose_name='Коментар', max_length=1000)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = '(Запити) Оренда полотна'

class CanvasRentedDates(models.Model):
    canvas_id = models.IntegerField(verbose_name='ID стелажа', default=0)
    name = models.CharField(verbose_name="Ім'я", max_length=255)
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    comentar = models.TextField(verbose_name='Коментар', max_length=1000)
    date_from = models.DateField(default=date.today)
    date_to = models.DateField(default=date.today)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)

    def __str__(self):
        return self.name + str(self.canvas_id)
    
    class Meta:
        verbose_name_plural = '(Зарезервовані) Оренда полотна'

class ShelvesRentedDates(models.Model):
    shelves_id = models.IntegerField(verbose_name='ID стелажа', default=0)
    name = models.CharField(verbose_name="Ім'я", max_length=255)
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    comentar = models.TextField(verbose_name='Коментар', max_length=1000)
    date_from = models.DateField(default=date.today)
    date_to = models.DateField(default=date.today)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)

    def __str__(self):
        return self.name + str(self.shelves_id)
    
    class Meta:
        verbose_name_plural = '(Зарезервовані) Оренда стелажів'
    
