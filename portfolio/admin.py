from django.contrib import admin
from .models import *
# Register your models here.


class profileAdmi(admin.ModelAdmin):
    list_display = ('id', 'Bio', 'skills_title', 'skills_description',)


admin.site.register(profile, profileAdmi)


class skillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_language',
                    'secon_language', 'icon_link',)


admin.site.register(skills, skillsAdmin)


class clientAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name',)


admin.site.register(client, clientAdmin)


class portfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'portfolio_title', 'company_name',)


admin.site.register(portfolio, portfolioAdmin)
