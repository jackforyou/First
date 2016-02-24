from django.contrib import admin

from .models import ChineseTable, FoodImage, SetMenu

class FoodImageInline(admin.TabularInline):
	model = FoodImage
	extra = 3

class SetMenuInline(admin.TabularInline):
	model = SetMenu
	extra = 3

class ChineseTableAdmin(admin.ModelAdmin):
    fieldsets = [
	(None,               {'fields': ['title_text']}),
	(None,               {'fields': ['image']}),
	(None,               {'fields': ['pub_date']}),
	(None,               {'fields': ['place_for_service_text']}),
	(None,               {'fields': ['location_text']}),
	(None,               {'fields': ['description_text']}),
	(None,               {'fields': ['price_start_number']}),
	(None,               {'fields': ['price_end_number']}),
	]
    inlines = [SetMenuInline, FoodImageInline]

admin.site.register(FoodImage)
admin.site.register(SetMenu)
admin.site.register(ChineseTable, ChineseTableAdmin)

# Register your models here.
