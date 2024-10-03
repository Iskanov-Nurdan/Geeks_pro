# Generated by Django 5.1 on 2024-08-21 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/', verbose_name='Фото товара '),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Названия товара '),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена товара '),
        ),
    ]
