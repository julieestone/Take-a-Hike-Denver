# Generated by Django 3.2 on 2021-04-24 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hike', '0008_alter_trail_hike_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='hike_image_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
