# Generated by Django 3.2.25 on 2024-06-01 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('armamentos', '0005_auto_20240530_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manutencao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now=True)),
                ('escalao', models.CharField(choices=[('1º Escalão', '1º Escalão'), ('2º Escalão', '2º Escalão'), ('3º Escalão', '3º Escalão'), ('4º Escalão', '4º Escalão')], default='1º Escalão', max_length=20, verbose_name='Escalão da Manutenção')),
                ('armamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manutencao', to='armamentos.armamento')),
            ],
        ),
    ]
