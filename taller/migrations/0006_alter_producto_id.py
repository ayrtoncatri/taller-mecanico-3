# Generated by Django 4.1.2 on 2023-06-26 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0005_remove_producto_codigo_producto_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
