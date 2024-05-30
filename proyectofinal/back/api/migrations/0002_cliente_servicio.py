# Generated by Django 5.0.3 on 2024-05-30 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('apellido', models.TextField()),
                ('cedula', models.TextField()),
                ('telefono', models.TextField()),
                ('email', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreServicio', models.TextField()),
                ('cedulaCliente', models.TextField()),
                ('descripcion', models.TextField()),
                ('precio', models.TextField()),
            ],
        ),
    ]
