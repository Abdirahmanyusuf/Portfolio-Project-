# Generated by Django 2.2.9 on 2020-07-17 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_auto_20200717_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='client_title',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='portfolio_title',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='skills_description',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='skills_title',
        ),
        migrations.AddField(
            model_name='client',
            name='client_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='portfolio_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='skills',
            name='skills_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='skills',
            name='skills_title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]