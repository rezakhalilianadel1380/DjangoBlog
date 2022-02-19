from django.contrib import admin

from nlg_category.models import Category

# Register your models here.

class Category_Admin(admin.ModelAdmin):
    list_display=['__str__','favorite']
    list_editable=['favorite']
    

admin.site.register(Category,Category_Admin)