# Generated by Django 5.1.4 on 2024-12-18 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0007_alter_hotel_city_alter_hotel_city_en_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('user_name', 'hotel')},
        ),
    ]
