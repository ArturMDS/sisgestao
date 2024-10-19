# Generated by Django 3.2.23 on 2024-07-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viaturas', '0004_alter_viatura_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='verificacoes',
            name='tipo',
            field=models.CharField(choices=[('Pneu', 'Pneu'), ('Óleo', 'Óleo'), ('Filtro', 'Filtro')], default='Pneu', max_length=25),
        ),
    ]
