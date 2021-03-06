# Generated by Django 3.1.5 on 2021-01-16 16:14

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210116_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='latitude',
            field=django_google_maps.fields.AddressField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='longitude',
            field=django_google_maps.fields.AddressField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
