# Generated by Django 4.2 on 2023-04-19 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0002_brand_alter_car_model"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="cars/"),
        ),
        migrations.AddField(
            model_name="car",
            name="plate",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
