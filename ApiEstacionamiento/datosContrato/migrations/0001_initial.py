# Generated by Django 4.0.3 on 2022-06-18 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_rename_rol_user_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosContrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(max_length=500)),
                ('nMeses', models.IntegerField()),
                ('nCuenta', models.CharField(max_length=20)),
                ('fechaInicio', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]