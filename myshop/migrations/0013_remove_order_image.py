# Generated by Django 4.1.5 on 2023-01-19 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0012_delete_baskets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='image',
        ),
    ]