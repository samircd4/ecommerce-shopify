# Generated by Django 4.1.3 on 2022-12-23 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cartorder_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.vendor'),
        ),
    ]
