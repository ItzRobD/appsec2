# Generated by Django 4.1.3 on 2022-11-12 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LegacySite', '0003_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image_path',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
