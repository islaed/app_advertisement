from django.contrib import admin
from .models import Advertisement
from django.utils.html import format_html


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price',
                    'created_date', 'updated_date', 'auction',
                    'display_image']
    list_filter = ['auction', 'created_at', 'updated_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return format_html('<img src="{}" width="50" height="50" />', '/static/img/adv.png')

    display_image.short_description = 'Изображение'

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)


admin.site.register(Advertisement, AdvertisementAdmin)
