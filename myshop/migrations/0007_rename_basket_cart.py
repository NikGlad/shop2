# Generated by Django 4.1.5 on 2023-01-13 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0006_basket'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Basket',
            new_name='Cart',
        ),
    ]
