# Generated by Django 5.0.7 on 2024-08-09 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_rename_bookingdate_booking_booking_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='reservation_slot',
            field=models.SmallIntegerField(default=10),
        ),
    ]
