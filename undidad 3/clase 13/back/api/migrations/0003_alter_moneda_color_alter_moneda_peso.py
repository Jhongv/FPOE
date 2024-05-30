
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_moneda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneda',
            name='color',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='peso',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='tamaño',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='valor',
            field=models.IntegerField(),
        ),
    ]
