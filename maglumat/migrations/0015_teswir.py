# Generated by Django 4.1.3 on 2022-12-01 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0014_remove_uniwersitetler_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='teswir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at', models.CharField(max_length=50)),
                ('beyan', models.TextField()),
                ('wagt', models.DateField()),
                ('uniwersitet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maglumat.uniwersitetler')),
            ],
        ),
    ]
