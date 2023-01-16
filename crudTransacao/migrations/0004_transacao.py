# Generated by Django 4.1.4 on 2023-01-15 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crudTransacao", "0003_person_age2"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transacao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("age", models.IntegerField(default=0)),
                ("age2", models.IntegerField(default=0)),
            ],
        ),
    ]
