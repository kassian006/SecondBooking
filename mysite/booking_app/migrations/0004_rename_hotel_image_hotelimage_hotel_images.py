# Generated by Django 5.1.4 on 2024-12-14 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0003_alter_hotel_city_alter_hotel_city_en_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelimage',
            old_name='hotel_image',
            new_name='hotel_images',
        ),
    ]