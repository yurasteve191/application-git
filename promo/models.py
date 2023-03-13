from django.db import models
from datetime import date

# class PromoCodes(models.Model):
#     PROMO_TYPE_CHOICES = [
#         ('date', 'Термін дії'),
#         ('count', 'К-сть застосувань'),
#     ]
#     promo_type = models.CharField(verbose_name='Термін дії', max_length=255, choices=PROMO_TYPE_CHOICES)
#     promo_discount = models.IntegerField(verbose_name='Знижка(%)', default=0)
#     promo_count = models.IntegerField(verbose_name='К-сть використань', default=0)
#     promo_count = models.DateField(verbose_name='Кінцевий термін дії', default=date.today)
#     promo_is_used = models.BooleanField(default=False)
    
#     created_at = models.CharField(max_length=255)

#     class Meta:
#         verbose_name_plural = 'Промокоди'