# Generated by Django 3.2.10 on 2022-01-07 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobilemodel',
            name='description',
        ),
        migrations.AddField(
            model_name='mobilemodel',
            name='order',
            field=models.TextField(default=''),
        ),
    ]
