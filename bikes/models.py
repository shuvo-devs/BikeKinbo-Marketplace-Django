from django.db import models
from ckeditor.fields import RichTextField


class Bike(models.Model):
    brands = (
        ("Bajaj", "Bajaj"),
        ("Yamaha", "Yamaha"),
        ("TVS", "TVS"),
        ("Royal Enfield", "Royal Enfield"),
    )
    tyres_types = (
        ("Tube", "Tube"),
        ("Tubeless", "Tubeless"),
    )
    wheels_types = (
        ("Spoke", "Spoke"),
        ("Alloy", "Alloy"),
    )
    divisions = (
        ("Dhaka", "Dhaka"),
        ("Chittagong", "Chittagong"),
        ("Rajshahi", "Rajshahi"),
        ("Khulna", "Khulna"),
        ("Barisal", "Barisal"),
        ("Sylhet", "Sylhet"),
        ("Rangpur", "Rangpur"),
    )
    districts = (
        ("Bagerhat", "Bagerhat"),
        ("Bandarban", "Bandarban"),
        ("Barguna", "Barguna"),
        ("Barisal", "Barisal"),
        ("Bhola", "Bhola"),
        ("Bogra", "Bogra"),
        ("Brahmanbaria", "Brahmanbaria"),
        ("Chandpur", "Chandpur"),
        ("Chapai Nawabganj", "Chapai Nawabganj"),
        ("Chattogram", "Chattogram"),
        ("Chuadanga", "Chuadanga"),
        ("Comilla", "Comilla"),
        ("Cox's Bazar", "Cox's Bazar"),
        ("Dhaka", "Dhaka"),
        ("Dinajpur", "Dinajpur"),
        ("Faridpur", "Faridpur"),
        ("Feni", "Feni"),
        ("Gaibandha", "Gaibandha"),
        ("Gazipur", "Gazipur"),
        ("Gopalganj", "Gopalganj"),
        ("Habiganj", "Habiganj"),
        ("Jamalpur", "Jamalpur"),
        ("Jashore", "Jashore"),
        ("Jhalokathi", "Jhalokathi"),
        ("Jhenaidah", "Jhenaidah"),
        ("Joypurhat", "Joypurhat"),
        ("Khagrachari", "Khagrachari"),
        ("Khulna", "Khulna"),
        ("Kishoreganj", "Kishoreganj"),
        ("Kurigram", "Kurigram"),
        ("Kushtia", "Kushtia"),
        ("Lakshmipur", "Lakshmipur"),
        ("Lalmonirhat", "Lalmonirhat"),
        ("Madaripur", "Madaripur"),
        ("Magura", "Magura"),
        ("Manikganj", "Manikganj"),
        ("Meherpur", "Meherpur"),
        ("Moulvibazar", "Moulvibazar"),
        ("Munshiganj", "Munshiganj"),
        ("Mymensingh", "Mymensingh"),
        ("Naogaon", "Naogaon"),
        ("Narail", "Narail"),
        ("Narayanganj", "Narayanganj"),
        ("Narsingdi", "Narsingdi"),
        ("Natore", "Natore"),
        ("Nawabganj", "Nawabganj"),
        ("Netrokona", "Netrokona"),
        ("Nilphamari", "Nilphamari"),
        ("Noakhali", "Noakhali"),
        ("Pabna", "Pabna"),
        ("Panchagarh", "Panchagarh"),
        ("Patuakhali", "Patuakhali"),
        ("Pirojpur", "Pirojpur"),
        ("Rajbari", "Rajbari"),
        ("Rajshahi", "Rajshahi"),
        ("Rangamati", "Rangamati"),
        ("Rangpur", "Rangpur"),
        ("Satkhira", "Satkhira"),
        ("Shariatpur", "Shariatpur"),
        ("Sherpur", "Sherpur"),
        ("Sirajganj", "Sirajganj"),
        ("Sunamganj", "Sunamganj"),
        ("Sylhet", "Sylhet"),
        ("Tangail", "Tangail"),
    )

    bike_name = models.CharField(max_length=255)
    brand = models.CharField(choices=brands, max_length=255)
    color = models.CharField(max_length=255)
    cc = models.IntegerField()
    year = models.IntegerField()
    mileage = models.IntegerField()
    fuel_capacity = models.IntegerField()
    driven = models.IntegerField()
    tyres_type = models.CharField(choices=tyres_types, max_length=255)
    wheels_type = models.CharField(choices=wheels_types, max_length=255)
    previous_owners = models.IntegerField()
    description = RichTextField(max_length=2000)
    division = models.CharField(choices=divisions, max_length=255)
    district = models.CharField(choices=districts, max_length=255)
    price = models.IntegerField()
    bike_photo_1 = models.ImageField(upload_to="photos/bikes/%y/%m/%d", blank=True)
    bike_photo_2 = models.ImageField(upload_to="photos/bikes/%y/%m/%d", blank=True)
    bike_photo_3 = models.ImageField(upload_to="photos/bikes/%y/%m/%d", blank=True)
    bike_photo_4 = models.ImageField(upload_to="photos/bikes/%y/%m/%d", blank=True)
    is_featured = models.BooleanField(default=False, verbose_name="Featured")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bike_name
