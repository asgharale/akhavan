# Generated by Django 5.1.3 on 2024-12-27 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='category',
            new_name='categories',
        ),
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='blog/thumbnails-%Y/'),
        ),
    ]
