# Generated by Django 5.1.3 on 2024-11-22 13:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_buyers_alter_product_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.discountgroup'),
        ),
    ]
