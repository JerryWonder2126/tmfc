# Generated by Django 3.1.5 on 2021-01-26 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210116_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='sub_title',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
