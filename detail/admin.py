

# Register your models here.
from django.contrib import admin
from . import models


@admin.register(models.Field)
class FieldAdmin(admin.ModelAdmin):
	list_display = [
        'location',
        ]

@admin.register(models.Crop)

class CropAdmin(admin.ModelAdmin):
	list_display = [
        'id',
        'name',
        'agricultural_Data'
        ]



@admin.register(models.Polygon)

class PolygonAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'location',
 ]
   