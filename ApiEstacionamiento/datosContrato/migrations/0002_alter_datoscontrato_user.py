# Generated by Django 4.0.3 on 2022-06-18 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_estacionamiento_user'),
        ('datosContrato', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datoscontrato',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.estacionamiento'),
        ),
    ]
