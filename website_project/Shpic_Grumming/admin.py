from django.contrib import admin
from django.utils.html import format_html
from .models import Breed, Dog

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'origin', 'image_tag')
    search_fields = ('name',)
    readonly_fields = ('image_tag',)
    fields = ('name', 'description', 'origin', 'image', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px; border-radius:8px;" />', obj.image.url)
        return '-'
    image_tag.short_description = 'Фото'

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'age', 'image_tag')
    list_filter = ('breed',)
    search_fields = ('name',)
    readonly_fields = ('image_tag',)
    fields = ('name', 'breed', 'age', 'description', 'image', 'image_tag', 'owner')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px; border-radius:8px;" />', obj.image.url)
        return '-'
    image_tag.short_description = 'Фото'
