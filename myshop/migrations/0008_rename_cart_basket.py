# Generated by Django 4.1.5 on 2023-01-18 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0007_rename_basket_cart'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='Basket',
        ),
    ]