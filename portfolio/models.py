from django.db import models

from datetime import datetime
# Create your models here.


class profile(models.Model):
    Bio = models.TextField(blank=True)
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    skills_title = models.CharField(max_length=200, blank=True)
    skills_description = models.TextField(blank=True)
    client_title = models.CharField(max_length=200, blank=True)


class skills(models.Model):
    title = models.CharField(max_length=200, blank=True)
    first_language = models.CharField(max_length=200, blank=True)
    secon_language = models.CharField(max_length=200, blank=True)
    icon_link = models.CharField(max_length=200, blank=True)


class client(models.Model):

    company_name = models.CharField(max_length=200, blank=True)
    company_logo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)


class portfolio(models.Model):
    portfolio_Desc = models.TextField(blank=True)
    portfolio_img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    portfolio_title = models.CharField(max_length=200, blank=True)
    company_name = models.CharField(max_length=200, blank=True)
