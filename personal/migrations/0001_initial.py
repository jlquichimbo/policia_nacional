# Generated by Django 3.1.6 on 2021-07-18 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(max_length=10)),
                ('apellidos', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('tipo_sangre', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('AB+', 'AB+'), ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB-', 'AB-')], max_length=3)),
                ('ciudad_nacimiento', models.CharField(max_length=50)),
                ('telefono_celular', models.CharField(max_length=10)),
                ('rango_grado', models.CharField(choices=[('1', 'Capitán'), ('2', 'Teniente'), ('3', 'Subteniente'), ('4', 'Sargento Primero'), ('5', 'Sargento Segundo'), ('6', 'Cabo Primero'), ('7', 'Cabo Segundo')], max_length=1)),
                ('dependencia', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
    ]