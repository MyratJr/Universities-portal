# Generated by Django 4.1.3 on 2022-12-05 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0029_alter_yurtlar_options_rename_at_yurtlar_at_tm'),
    ]

    operations = [
        migrations.AddField(
            model_name='yurtlar',
            name='at_en',
            field=models.CharField(default=1, max_length=50),
        ),
        migrations.AddField(
            model_name='yurtlar',
            name='at_ru',
            field=models.CharField(default=1, max_length=50),
        ),
    ]