# Generated by Django 4.1.5 on 2023-01-27 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_category_valor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='valor',
        ),
    ]
