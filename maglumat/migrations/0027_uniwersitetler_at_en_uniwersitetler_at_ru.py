# Generated by Django 4.1.3 on 2022-12-03 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0026_alter_uniwersitetler_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='uniwersitetler',
            name='at_en',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AddField(
            model_name='uniwersitetler',
            name='at_ru',
            field=models.CharField(default=1, max_length=200),
        ),
    ]
