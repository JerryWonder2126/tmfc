# Generated by Django 3.1.4 on 2021-01-14 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210114_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='title',
            field=models.CharField(max_length=40, null=True, unique=True),
        ),
    ]
