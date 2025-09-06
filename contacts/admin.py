from django.contrib import admin
from .models import *


class InquiryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email_address",
        "phone_number",
        "district",
        "division",
        "created_date",
    )
    list_display_links = (
        "id",
        "first_name",
        "last_name",
        "email_address",
    )
    search_fields = (
        "id",
        "first_name",
        "last_name",
        "email_address",
        "phone_number",
    )
    readonly_fields = (
        "user_id",
        "first_name",
        "last_name",
        "email_address",
        "phone_number",
        "district",
        "division",
        "message",
        "bike_id",
        "bike_name",
    )
    list_per_page = 25


class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "subject", "email_address", "phone_number")
    list_display_links = (
        "id",
        "full_name",
    )
    search_fields = ("id", "full_name", "email_address", "phone_number")
    readonly_fields = (
        "full_name",
        "subject",
        "email_address",
        "phone_number",
        "message",
    )


admin.site.register(Inquiry, InquiryAdmin)
admin.site.register(Message, MessageAdmin)
