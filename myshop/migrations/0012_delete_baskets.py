# Generated by Django 4.1.5 on 2023-01-19 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0011_rename_basket_baskets'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Baskets',
        ),
    ]
