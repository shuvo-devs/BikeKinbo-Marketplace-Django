from django.contrib import admin
from .models import *
from django.utils.html import format_html


class BikeAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(
            "<img src={} style='border-radius: 5px' width='50px'/>".format(
                object.bike_photo_1.url
            )
        )

    thumbnail.short_description = "Photo"

    list_display = (
        "id",
        "thumbnail",
        "bike_name",
        "brand",
        "cc",
        "color",
        "year",
        "previous_owners",
        "price",
        "district",
        "is_featured",
        "created_date",
    )
    list_display_links = ("bike_name",)
    list_editable = ("is_featured",)
    list_filter = (
        "brand",
        "cc",
        "color",
        "year",
        "district",
    )


admin.site.register(Bike, BikeAdmin)
