# Generated by Django 4.1.7 on 2023-03-05 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_orders_ordertransactionid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='created_at',
            field=models.CharField(max_length=255),
        ),
    ]
