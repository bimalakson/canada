# Generated by Django 4.0.1 on 2022-02-09 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaksi', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='placeholder.png', null=True, upload_to=''),
        ),
    ]
