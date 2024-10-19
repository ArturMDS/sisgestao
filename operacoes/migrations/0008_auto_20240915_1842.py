# Generated by Django 3.2.23 on 2024-09-15 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operacoes', '0007_auto_20240915_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planoembarque',
            old_name='chegada',
            new_name='inicio',
        ),
        migrations.RemoveField(
            model_name='planoembarque',
            name='partida',
        ),
        migrations.AddField(
            model_name='operacional',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='planoembarque',
            name='comboio',
            field=models.CharField(default=0, max_length=50, verbose_name='Nome do comboio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planoembarque',
            name='efetivo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='planoembarqueviatura',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='planoembarque',
            name='atividade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plano_embarque', to='operacoes.atividade'),
        ),
    ]
