# Generated by Django 2.2 on 2020-02-27 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('cat1', models.CharField(blank=True, max_length=25)),
                ('cat2', models.CharField(blank=True, max_length=25)),
                ('image', models.CharField(choices=[('bees_knees_small.jpg', "Bee's Knees"), ('french75.jpg', 'French 75'), ('south_side_fizz.jpg', 'South Side Fizz'), ('tonic_and_gin.jpg', 'Tonic and Gin'), ('ward8.jpg', 'Ward 8')], default='bees_knees_small.jpg', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Candle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('style', models.CharField(choices=[('Jar', 'Jar'), ('Melt', 'Melt')], default='Jar', max_length=25)),
                ('image', models.CharField(choices=[('bees_knees_small.jpg', "Bee's Knees"), ('french75.jpg', 'French 75'), ('south_side_fizz.jpg', 'South Side Fizz'), ('tonic_and_gin.jpg', 'Tonic and Gin'), ('ward8.jpg', 'Ward 8')], default='bees_knees_small.jpg', max_length=50)),
                ('in_stock', models.SmallIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('scent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candles', to='inventory_app.Scent')),
            ],
        ),
    ]
