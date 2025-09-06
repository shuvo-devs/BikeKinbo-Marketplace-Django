from django.db import models


class Inquiry(models.Model):
    user_id = models.IntegerField(blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=18)
    district = models.CharField(max_length=255)
    division = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    bike_id = models.IntegerField()
    bike_name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Inquiry"
        verbose_name_plural = "Inquiries"


class Message(models.Model):
    full_name = models.CharField(max_length=255)
    email_address = models.EmailField()
    subject = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=18)
    message = models.TextField(null=True)
