# Generated by Django 4.1.2 on 2023-06-25 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0002_remove_producto_cantidad_remove_producto_codigo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
