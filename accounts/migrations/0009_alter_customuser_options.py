# Generated by Django 4.1.6 on 2023-02-07 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_customuser_profile_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['-username']},
        ),
    ]
