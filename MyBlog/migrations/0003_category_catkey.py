# Generated by Django 2.2.1 on 2019-05-14 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0002_auto_20190513_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='catKey',
            field=models.CharField(default=3, max_length=16),
            preserve_default=False,
        ),
    ]
