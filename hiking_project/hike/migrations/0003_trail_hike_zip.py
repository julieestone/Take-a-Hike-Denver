# Generated by Django 3.2 on 2021-04-22 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hike', '0002_auto_20210421_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='hike_zip',
            field=models.CharField(default=80014, max_length=5),
            preserve_default=False,
        ),
    ]
