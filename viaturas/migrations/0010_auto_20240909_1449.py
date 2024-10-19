# Generated by Django 3.2.23 on 2024-09-09 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viaturas', '0009_alteracao_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dadostecnicos',
            name='viatura',
        ),
        migrations.RemoveField(
            model_name='viatura',
            name='classificacao',
        ),
        migrations.AddField(
            model_name='dadostecnicos',
            name='classificacao',
            field=models.CharField(choices=[('Vtr 3/4 Ton', 'Vtr 3/4 Ton'), ('Vtr 1 e 1/2 Ton', 'Vtr 1 e 1/2 Ton'), ('Vtr 5 Ton', 'Vtr 5 Ton'), ('Vtr 7 Ton', 'Vtr 7 Ton'), ('Vtr 10 Ton', 'Vtr 10 Ton'), ('Vtr Bld', 'Vtr Bld'), ('Ambulância Op', 'Ambulância Op'), ('Ambulância Adm', 'Ambulância Adm'), ('Vtr Adm', 'Vtr Adm'), ('Reboque Cistena', 'Reboque Cistena'), ('Vtr Cisterna', 'Vtr Cisterna'), ('Ônibus', 'Ônibus'), ('Cozinha de Campanha', 'Cozinha de Campanha'), ('Vtr Basculante', 'Vtr Basculante'), ('Outros', 'Outros')], default='Outros', max_length=50),
        ),
        migrations.AddField(
            model_name='viatura',
            name='dados_tecnicos',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='viatura', to='viaturas.dadostecnicos'),
            preserve_default=False,
        ),
    ]
