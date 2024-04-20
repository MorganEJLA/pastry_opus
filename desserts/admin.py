from django.contrib import admin
from .models import Dessert, Locale, Ingredient, IngredientVariation, DessertVariation
from django.utils.html import format_html

class DessertVariationInline(admin.StackedInline):
    model = DessertVariation
    extra = 0

class IngredientVariationInline(admin.StackedInline):
    model = IngredientVariation
    extra = 0

class DessertAdmin(admin.ModelAdmin):
    inlines = [DessertVariationInline]

    def dessert_thumbnail(self, obj):
        return format_html('<img src="{}" width="40" />'.format(obj.dessert_photo.url))
    dessert_thumbnail.short_description = "Photo"

    def get_locale_names(self, obj):
        return ", ".join(locale.name for locale in obj.locale_name.all()) if obj.locale_name.exists() else ""

    def get_ingredient_names(self, obj):
        return ", ".join(ingredient.name for ingredient in obj.featured_ingredient.all()) if obj.featured_ingredient.exists() else ""

    get_ingredient_names.short_description = "Ingredient Name"
    get_locale_names.short_description = "Locale Name"

    list_display = ("id", "dessert_name", "get_locale_names", "dessert_thumbnail", "get_ingredient_names", "is_featured")
    list_display_links = ("id", "dessert_name", "get_locale_names")
    search_fields = ("dessert_name", "locale_name__name", "featured_ingredient__name")
    list_filter = ("dessert_name",)
    autocomplete_fields = ["locale_name", "featured_ingredient"]
    ordering = ("locale_name", "dessert_name")

class LocaleAdmin(admin.ModelAdmin):
    def locale_thumbnail(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.banner_photo.url))
    locale_thumbnail.short_description = "Photo"

    list_display = ("id", "name", "locale_thumbnail")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("name",)

class IngredientAdmin(admin.ModelAdmin):
    def ingredient_thumbnail(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))
    ingredient_thumbnail.short_description = "Photo"

    list_display = ("id", "name", "ingredient_thumbnail")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("name",)
    ordering  = ("name",)

class DessertVariationAdmin(admin.ModelAdmin):
    def dessert_thumbnail(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.image.url))
    dessert_thumbnail.short_description = "Photo"
    list_display = ('id', 'dessert', 'name', 'locale', 'preparation_method', 'dessert_thumbnail')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'locale__name')
    list_filter = ('locale',)

admin.site.register(Locale, LocaleAdmin)
admin.site.register(Dessert, DessertAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(DessertVariation, DessertVariationAdmin)
