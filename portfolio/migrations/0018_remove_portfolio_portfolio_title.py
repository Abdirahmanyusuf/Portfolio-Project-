# Generated by Django 2.2.9 on 2020-07-17 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_auto_20200717_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='portfolio_title',
        ),
    ]
