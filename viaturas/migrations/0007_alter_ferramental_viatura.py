# Generated by Django 3.2.23 on 2024-07-09 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viaturas', '0006_auto_20240709_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ferramental',
            name='viatura',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ferramental', to='viaturas.viatura'),
        ),
    ]
