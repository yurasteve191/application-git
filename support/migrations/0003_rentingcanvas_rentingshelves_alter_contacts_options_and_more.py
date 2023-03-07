# Generated by Django 4.1.7 on 2023-03-06 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentingCanvas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="Ім'я")),
                ('desctiprion', models.TextField(max_length=1000, verbose_name='Опис')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('rate', models.IntegerField(verbose_name='Оцінка')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
            ],
            options={
                'verbose_name_plural': 'Оренда полотна',
            },
        ),
        migrations.CreateModel(
            name='RentingShelves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="Ім'я")),
                ('desctiprion', models.TextField(max_length=1000, verbose_name='Опис')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('rate', models.IntegerField(verbose_name='Оцінка')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
            ],
            options={
                'verbose_name_plural': 'Оренда стелажів',
            },
        ),
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name_plural': 'Контакти'},
        ),
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name_plural': 'Відгуки'},
        ),
        migrations.AlterField(
            model_name='contacts',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата створення'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='name',
            field=models.CharField(max_length=255, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата створення'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='desctiprion',
            field=models.TextField(max_length=1000, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=255, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rate',
            field=models.IntegerField(verbose_name='Оцінка'),
        ),
    ]
