# Generated by Django 4.1.2 on 2023-06-26 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0007_producto_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='id',
        ),
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
