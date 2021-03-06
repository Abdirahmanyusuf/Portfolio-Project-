# Generated by Django 2.2.9 on 2020-07-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20200716_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='description',
            new_name='Bio',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='skills_Four',
            new_name='development_type',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='skills_Three',
            new_name='development_type1',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='title2',
            new_name='development_type2',
        ),
        migrations.AddField(
            model_name='profile',
            name='skiills_three',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='skiills_two',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='skill_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='skills_One',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='skills_three',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
