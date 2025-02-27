# Generated by Django 3.2.23 on 2024-07-08 00:59

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('viaturas', '0002_auto_20240706_1939'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='viatura',
            managers=[
                ('objescts', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='disponibilidade',
            name='situacao',
            field=models.CharField(choices=[('Disponível', 'Disp'), ('Indisponível', 'Insdisp'), ('Descarregado', 'Descarregado'), ('Disponível com Restrição', 'Disp com Restrição')], default='Disponível', max_length=40),
        ),
        migrations.AlterField(
            model_name='itemferramental',
            name='situacao',
            field=models.CharField(choices=[('Disponível', 'Disp'), ('Indisponível', 'Insdisp'), ('Descarregado', 'Descarregado'), ('Disponível com Restrição', 'Disp com Restrição')], default='Disponível', max_length=40),
        ),
        migrations.AlterField(
            model_name='verificacaosituacao',
            name='situacao',
            field=models.CharField(choices=[('Disponível', 'Disp'), ('Indisponível', 'Insdisp'), ('Descarregado', 'Descarregado'), ('Disponível com Restrição', 'Disp com Restrição')], default='Disponível', max_length=40),
        ),
        migrations.AlterField(
            model_name='viatura',
            name='classificacao',
            field=models.CharField(choices=[('Vtr 3/4 Ton', 'Vtr 3/4 Ton'), ('Vtr 1 e 1/2 Ton', 'Vtr 1 e 1/2 Ton'), ('Vtr 5 Ton', 'Vtr 5 Ton'), ('Vtr 7 Ton', 'Vtr 7 Ton'), ('Vtr 10 Ton', 'Vtr 10 Ton'), ('Vtr Bld', 'Vtr Bld'), ('Ambulância Op', 'Ambulância Op'), ('Ambulância Adm', 'Ambulância Adm'), ('Vtr Adm', 'Vtr Adm'), ('Reboque Cistena', 'Reboque Cistena'), ('Vtr Cisterna', 'Vtr Cisterna'), ('Ônibus', 'Ônibus'), ('Cozinha de Campanha', 'Cozinha de Campanha'), ('Vtr Basculante', 'Vtr Basculante'), ('Outros', 'Outros')], default='Outros', max_length=50),
        ),
    ]
