# Generated by Django 3.1.7 on 2021-04-12 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_blog_post_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
