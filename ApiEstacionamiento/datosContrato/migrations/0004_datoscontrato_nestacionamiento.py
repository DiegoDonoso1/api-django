# Generated by Django 4.0.3 on 2022-06-22 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datosContrato', '0003_rename_user_datoscontrato_estacionamiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='datoscontrato',
            name='nEstacionamiento',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
