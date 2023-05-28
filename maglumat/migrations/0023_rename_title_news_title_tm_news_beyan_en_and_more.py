# Generated by Django 4.1.3 on 2022-12-03 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0022_rename_beyan_news_beyan_tm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='title',
            new_name='title_tm',
        ),
        migrations.AddField(
            model_name='news',
            name='beyan_en',
            field=models.TextField(default=1),
        ),
        migrations.AddField(
            model_name='news',
            name='beyan_ru',
            field=models.TextField(default=1),
        ),
    ]