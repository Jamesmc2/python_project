# Generated by Django 2.2 on 2020-02-27 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0004_address_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]