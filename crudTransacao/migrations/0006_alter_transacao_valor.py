# Generated by Django 4.1.4 on 2023-01-29 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudTransacao', '0005_alter_transacao_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True),
        ),
    ]
