# Generated by Django 2.2 on 2020-02-27 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
        ('inventory_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candle',
            name='favorited_by',
            field=models.ManyToManyField(related_name='favorites', to='login_app.User'),
        ),
    ]