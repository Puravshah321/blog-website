# Generated by Django 5.1.2 on 2024-12-29 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_alter_post_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=100000),
        ),
    ]
