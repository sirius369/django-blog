# Generated by Django 2.0 on 2020-01-26 10:41

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200126_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.FileField(default='none.jpg', upload_to=post.models.user_directory_path),
        ),
    ]
