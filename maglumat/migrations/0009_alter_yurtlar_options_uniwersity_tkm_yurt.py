# Generated by Django 4.1.3 on 2022-12-01 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0008_yurtlar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='yurtlar',
            options={'ordering': ['at']},
        ),
        migrations.AddField(
            model_name='uniwersity_tkm',
            name='yurt',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='maglumat.yurtlar'),
        ),
    ]
