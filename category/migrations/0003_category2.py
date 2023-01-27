# Generated by Django 4.1.5 on 2023-01-27 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_category_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('descricao', models.TextField()),
                ('tipoTransacao', models.BooleanField(default=0)),
            ],
        ),
    ]