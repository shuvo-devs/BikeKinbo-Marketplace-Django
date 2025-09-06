from django.contrib import admin
from .models import *
from django.utils.html import format_html
from solo.admin import SingletonModelAdmin


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(
            "<img src={} style='border-radius: 5px' width='50px'/>".format(
                object.photo.url
            )
        )

    thumbnail.short_description = "Photo"

    list_display = (
        "id",
        "thumbnail",
        "first_name",
        "last_name",
        "designation",
        "created_date",
    )
    list_display_links = ("thumbnail", "first_name", "last_name")
    list_filter = ("designation",)
    search_fields = (
        "id",
        "first_name",
        "last_name",
        "designation",
    )


class SettingAdmin(SingletonModelAdmin):
    pass


admin.site.register(Team, TeamAdmin)
admin.site.register(Setting, SettingAdmin)
