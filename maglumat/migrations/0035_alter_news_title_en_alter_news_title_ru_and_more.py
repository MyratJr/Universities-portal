# Generated by Django 4.1.3 on 2022-12-05 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0034_alter_news_title_en_alter_news_title_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_tm',
            field=models.CharField(max_length=100),
        ),
    ]