# Generated by Django 4.1.6 on 2023-02-07 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_country_customuser_profile_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, default='default_profile_picture.jpg', null=True, upload_to='profile_pics'),
        ),
    ]