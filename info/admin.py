from django.contrib import admin
from django.utils.html import format_html
from .models import News, TopNews, Actions, Music

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'thumbnail_html', 'short_description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'short_description', 'full_description')

    def thumbnail_html(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="100" height="auto"/>')
        else:
            return "-"
    
    thumbnail_html.short_description = "Мініатюра"

@admin.register(Actions)
class ActionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'thumbnail_html', 'short_description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'short_description', 'full_description')

    def thumbnail_html(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="100" height="auto"/>')
        else:
            return "-"
    
    thumbnail_html.short_description = "Мініатюра"
    
@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'thumbnail_html', 'short_description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'short_description', 'full_description')

    def thumbnail_html(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="100" height="auto"/>')
        else:
            return "-"
    
    thumbnail_html.short_description = "Мініатюра"
    

@admin.register(TopNews)
class TopNewsAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_html', 'short_description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('short_description',)

    def thumbnail_html(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="100" height="auto"/>')
        else:
            return "-"
    
    thumbnail_html.short_description = "Мініатюра"



admin.site.site_header='Адмін панель - Інформатика'
admin.site.site_title='Інформатика'