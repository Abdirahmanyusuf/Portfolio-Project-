# Generated by Django 2.2.9 on 2020-07-16 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20200716_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tool_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='tool_title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
