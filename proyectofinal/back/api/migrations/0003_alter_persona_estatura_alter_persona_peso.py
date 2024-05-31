# Generated by Django 5.0.3 on 2024-04-17 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_persona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='estatura',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='persona',
            name='peso',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
