# Generated by Django 5.1.2 on 2024-12-30 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_alter_category_options_alter_comment_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.CharField(blank=True, default='30 December 2024', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.CharField(blank=True, default='30 December 2024', max_length=100),
        ),
    ]
