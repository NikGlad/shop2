# Generated by Django 4.1.5 on 2023-01-20 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0013_remove_order_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
