# Generated by Django 4.1.3 on 2022-12-02 14:20

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0016_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+99363591250', max_length=128, region=None),
        ),
    ]
