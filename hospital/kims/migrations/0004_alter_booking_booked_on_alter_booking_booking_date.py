# Generated by Django 5.0.1 on 2024-01-25 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kims', '0003_alter_booking_booked_on_alter_booking_booking_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booked_on',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(),
        ),
    ]
