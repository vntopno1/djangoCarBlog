# Generated by Django 4.1.5 on 2023-02-01 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0002_remove_blog_contenttwo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='reviews',
            new_name='contentTwo',
        ),
        migrations.AddField(
            model_name='blog',
            name='ingredients',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='postlabel',
            field=models.CharField(blank=True, choices=[('POPULAR', 'Popular')], max_length=100, null=True),
        ),
    ]