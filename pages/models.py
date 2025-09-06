from django.db import models
from ckeditor.fields import RichTextField
from solo.models import SingletonModel


class Team(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photos/teams/%y/%m/%d")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Setting(SingletonModel):
    company_phone_number = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    company_email = models.EmailField()
    company_fax = models.CharField(max_length=255)
    facebook_link = models.CharField(max_length=255)
    twitter_link = models.CharField(max_length=255)
    instagram_link = models.CharField(max_length=255)
    youtube_link = models.CharField(max_length=255)
    linkedin_link = models.CharField(max_length=255)
    index_banner_heading = models.CharField(max_length=255)
    index_banner_sub_heading = models.CharField(max_length=255)
    services_heading = models.CharField(max_length=255)
    services_text = RichTextField()
    services_video_link = models.CharField(max_length=255)
    footer_company_text = RichTextField()
    about_us_text = RichTextField()
    about_us_photo_1 = models.ImageField(
        upload_to="Photos/about_us/%y/%m/%d", blank=True
    )
    about_us_photo_2 = models.ImageField(
        upload_to="Photos/about_us/%y/%m/%d", blank=True
    )
    about_us_photo_3 = models.ImageField(
        upload_to="Photos/about_us/%y/%m/%d", blank=True
    )
    about_us_photo_4 = models.ImageField(
        upload_to="Photos/about_us/%y/%m/%d", blank=True
    )

    page_name = "Site Settings"

    def __str__(self):
        return self.page_name

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
