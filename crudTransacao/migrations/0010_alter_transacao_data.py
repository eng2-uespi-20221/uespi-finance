# Generated by Django 4.1.5 on 2023-01-27 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudTransacao', '0009_alter_transacao_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateField(null=True),
        ),
    ]
