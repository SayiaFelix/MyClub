# Generated by Django 4.0.4 on 2022-05-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_venue_email_address_alter_venue_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='zip_code',
            field=models.CharField(blank=True, max_length=15, verbose_name='Zip Code'),
        ),
    ]
