# Generated by Django 5.0.4 on 2024-04-12 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(blank=True, max_length=50)),
                ('peso', models.TextField(blank=True, max_length=5000)),
                ('tamaño', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('color', models.DateTimeField(auto_now=True, verbose_name='date updated')),
            ],
        ),
    ]
