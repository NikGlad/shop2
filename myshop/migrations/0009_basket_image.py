# Generated by Django 4.1.5 on 2023-01-19 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0008_rename_cart_basket'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/%Y/%m/%d'),
        ),
    ]
