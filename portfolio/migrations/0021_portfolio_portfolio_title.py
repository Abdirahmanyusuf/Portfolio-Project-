# Generated by Django 2.2.9 on 2020-07-17 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0020_auto_20200717_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='portfolio_title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
