# Generated by Django 3.2.25 on 2024-05-15 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armamentos', '0002_alter_armamento_unidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='alteracao',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
