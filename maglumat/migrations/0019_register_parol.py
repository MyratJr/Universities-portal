# Generated by Django 4.1.3 on 2022-12-02 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0018_alter_register_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='parol',
            field=models.CharField(default=7, max_length=8),
        ),
    ]