from django.contrib import admin

from .models import *

class UstozAdmin(admin.ModelAdmin):
    list_display = ["ism", "jins", "yosh", "daraja", "fan"]
    search_fields = ["ism"]
    search_help_text = "Ism bo'yicha qidiruv"


class YonalishAdmin(admin.ModelAdmin):
    list_display = ["nom", "active"]
    search_fields = ["nom"]
    search_help_text = "Nomi bo'yicha qidiruv"
    list_filter = ["active"]


class FanAdmin(admin.ModelAdmin):
    list_display = ["nom", "yonalish"]
    list_filter = ["yonalish__active", "yonalish__nom"]
    search_fields = ["nom"]
    search_help_text = "Nom bo'yicha qidiruv"


admin.site.register(Yonalish, YonalishAdmin)
admin.site.register(Fan, FanAdmin)
admin.site.register(Ustoz, UstozAdmin)

