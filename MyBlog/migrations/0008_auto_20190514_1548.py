# Generated by Django 2.2.1 on 2019-05-14 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0007_auto_20190514_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='artCatID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.Group', verbose_name='catName'),
        ),
    ]