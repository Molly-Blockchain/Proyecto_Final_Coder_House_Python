# Generated by Django 4.0.5 on 2022-07-05 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreLibro', models.CharField(max_length=100)),
                ('anioPublicacion', models.IntegerField()),
                ('genero', models.CharField(max_length=100)),
                ('fechaIngreso', models.DateField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bibliotecario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreBibliotecario', models.CharField(max_length=50)),
                ('apellidoBibliotecario', models.CharField(max_length=40)),
            ],
        ),
    ]
