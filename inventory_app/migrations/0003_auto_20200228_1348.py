# Generated by Django 2.2 on 2020-02-28 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0002_auto_20200228_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candle',
            name='image',
            field=models.CharField(choices=[('bees_knees_small.jpg', "Bee's Knees"), ('french75.jpg', 'French 75'), ('south_side_fizz.jpg', 'South Side Fizz'), ('tonic_and_gin.jpg', 'Tonic and Gin'), ('ward8.jpg', 'Ward 8'), ('repair-shop.jpg', 'Auto Shop'), ('the_beach.jpg', 'The Beach'), ('ThunderCats.jpg', 'Thunder Cats'), ('mailman.cologne.jpg', 'Mailman Wearing Cologne')], default='bees_knees_small.jpg', max_length=50),
        ),
        migrations.AlterField(
            model_name='scent',
            name='image',
            field=models.CharField(choices=[('bees_knees_small.jpg', "Bee's Knees"), ('french75.jpg', 'French 75'), ('south_side_fizz.jpg', 'South Side Fizz'), ('tonic_and_gin.jpg', 'Tonic and Gin'), ('ward8.jpg', 'Ward 8'), ('repair-shop.jpg', 'Auto Shop'), ('the_beach.jpg', 'The Beach'), ('ThunderCats.jpg', 'Thunder Cats'), ('mailman.cologne.jpg', 'Mailman Wearing Cologne')], default='bees_knees_small.jpg', max_length=50),
        ),
    ]
