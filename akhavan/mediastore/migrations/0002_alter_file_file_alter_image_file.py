# Generated by Django 5.1.3 on 2024-12-27 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediastore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.ImageField(upload_to='media/etc/%Y-%m/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(upload_to='media/img/%Y-%m/'),
        ),
    ]
