# Generated by Django 5.1.2 on 2024-12-29 10:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_alter_comment_content_alter_comment_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category'),
        ),
    ]
