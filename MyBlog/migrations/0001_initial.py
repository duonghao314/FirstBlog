# Generated by Django 2.2.1 on 2019-05-13 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catName', models.CharField(max_length=20)),
                ('catDecription', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
