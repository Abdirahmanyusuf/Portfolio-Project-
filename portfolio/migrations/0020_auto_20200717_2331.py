# Generated by Django 2.2.9 on 2020-07-17 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_auto_20200717_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='client_title',
        ),
        migrations.AddField(
            model_name='profile',
            name='client_title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
