# Generated by Django 4.1.2 on 2024-05-29 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0005_producto_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
    ]
