# Generated by Django 4.1.3 on 2022-12-03 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0021_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='beyan',
            new_name='beyan_tm',
        ),
    ]
