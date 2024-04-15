from django.contrib import admin
from .models import Chef
from django.utils.html import format_html

# Register your models here.
class ChefAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))
    thumbnail.short_description = "Photo"

    def icon_thumbnail(self, object):
        return format_html(f'<img src="{object.icon.url}" width="40" style="border-radius: 50%;">')

    thumbnail.short_description = "Icon"

    list_display = ("id", "full_name","thumbnail","locale", "title", "icon_thumbnail")
    list_display_links = ("id", "full_name")
    search_fields = ("full_name", "locale")
    list_filter = ("locale",)

admin.site.register(Chef, ChefAdmin)
