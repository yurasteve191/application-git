from django.contrib import admin
from django.utils.html import format_html
from .models import News,TopNews

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_html', 'short_description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'short_description', 'full_description')

    def thumbnail_html(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="100" height="auto"/>')
        else:
            return "-"
    
    thumbnail_html.short_description = "Thumbnail"
    

@admin.register(TopNews)
class TopNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_html', 'short_description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'short_description')

    def thumbnail_html(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="100" height="auto"/>')
        else:
            return "-"
    
    thumbnail_html.short_description = "Thumbnail"
