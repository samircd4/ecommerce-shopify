# Generated by Django 4.1.6 on 2023-02-02 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_address_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]