# Generated by Django 4.1.6 on 2023-02-02 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_product_life_product_mfd_product_stock_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(default=1, max_length=200, null=True),
        ),
    ]
