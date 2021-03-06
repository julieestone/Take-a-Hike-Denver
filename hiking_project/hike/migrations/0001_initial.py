# Generated by Django 3.2 on 2021-04-21 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hike_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Trail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trail_name', models.CharField(max_length=200)),
                ('hike_location', models.CharField(max_length=200)),
                ('hike_difficulty', models.CharField(max_length=20)),
                ('hike_milage', models.DecimalField(decimal_places=1, max_digits=2)),
                ('hike_description', models.CharField(max_length=1000)),
                ('hike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trails', to='hike.hike')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(max_length=20)),
                ('review', models.CharField(max_length=2000)),
                ('alias', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('trail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='hike.trail')),
            ],
        ),
    ]
