# Generated by Django 2.2.1 on 2019-05-17 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0010_article_artview'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='catViews',
            field=models.IntegerField(default=0),
        ),
    ]