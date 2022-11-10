from django.contrib import admin
from .models import Pharmacy, Pills, PillsCategory, Info


class PharmacyAdmin(admin.ModelAdmin):
    list_display = ("number", "location", "metro_station")
    search_fields = ("number", "location", "metro_station")


class PillsAdmin(admin.ModelAdmin):
    list_display = ("name", "doze", "amount", "creator", "receptRequired", "price", "category")
    list_display_links = ("name", "creator")
    search_fields = ("name", "doze", "amount", "creator", "receptRequired", "price")


class InfoAdmin(admin.ModelAdmin):
    list_display = ("pharmacy", "pills", "amount")
    search_fields = ("pharmacy", "pills", "amount")


admin.site.register(Pharmacy, PharmacyAdmin)
admin.site.register(Pills, PillsAdmin)
admin.site.register(PillsCategory)
admin.site.register(Info, InfoAdmin)

# Register your models here.
