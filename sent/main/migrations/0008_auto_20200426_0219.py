# Generated by Django 3.0.5 on 2020-04-25 20:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200426_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorialseries',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='category/images'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 26, 2, 19, 32, 406688), verbose_name='date'),
        ),
    ]
