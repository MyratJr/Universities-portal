# Generated by Django 4.1.3 on 2022-12-05 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0030_yurtlar_at_en_yurtlar_at_ru'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='yurtlar',
            options={'ordering': ['at']},
        ),
        migrations.RenameField(
            model_name='yurtlar',
            old_name='at_tm',
            new_name='at',
        ),
        migrations.RemoveField(
            model_name='yurtlar',
            name='at_en',
        ),
        migrations.RemoveField(
            model_name='yurtlar',
            name='at_ru',
        ),
    ]