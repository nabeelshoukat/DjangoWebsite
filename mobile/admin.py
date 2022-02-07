from django.contrib import admin
from .models import MobileModel,News

# Register your models here.
class MobileAdmin(admin.ModelAdmin):
    list_display = ("brand","price","color",'order')

admin.site.register(MobileModel,MobileAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ("news_title","news_description")

admin.site.register(News,NewsAdmin)

