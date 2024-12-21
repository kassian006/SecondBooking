# Generated by Django 5.1.4 on 2024-12-14 08:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0006_alter_hotel_city_alter_hotel_city_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotels', to='booking_app.city'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='city_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hotels', to='booking_app.city'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='city_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hotels', to='booking_app.city'),
        ),
    ]