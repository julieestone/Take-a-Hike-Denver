# Generated by Django 3.2 on 2021-04-24 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hike', '0004_auto_20210422_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='hike_image',
            field=models.ImageField(default='000', upload_to=''),
        ),
    ]
