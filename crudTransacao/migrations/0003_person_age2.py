# Generated by Django 4.1.4 on 2023-01-15 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crudTransacao", "0002_person_age"),
    ]

    operations = [
        migrations.AddField(
            model_name="person", name="age2", field=models.IntegerField(default=0),
        ),
    ]