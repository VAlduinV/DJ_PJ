from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from .models import *


class mainAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')  # поисковая система в админ-панели
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}  # URL слагов
    fields = ('title', 'slug', 'tech', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Мініатюра"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)  # обязательно , ибо кортеж
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(main, mainAdmin)  # Модель, вспомогательный класс
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Администратирование V.H.V'
admin.site.site_header = 'Администратирование веб-сайта V.H.V'
