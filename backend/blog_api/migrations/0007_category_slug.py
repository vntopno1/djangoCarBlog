# Generated by Django 4.1.5 on 2023-02-05 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0006_remove_blog_post_date_blog_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
