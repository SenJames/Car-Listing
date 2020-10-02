"""
Importing the modules needed for this project
"""
from django.conf import settings
from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


# Create your models here.



class UserProfile(models.Model):
    """
    Creating the Model for the Car Lisiting Site Alone
    """

    SELLER = (
        ('dealer', 'Dealer'),
        ('private','Private'),
    )

    profile_age = models.PositiveIntegerField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='media/', blank=True, null=True)
    profile_user = models.OneToOneField(User, on_delete=models.CASCADE, default=7)
    # profile_user = models.ForeignKey(User, on_delete=models.CASCADE, default=7, blank=True, null=True)
    profile_phone = PhoneNumberField(blank=True, null=True)
    profile_seller = models.CharField(max_length=100, choices=SELLER, default='Dealer')
    date_joined = models.DateTimeField(auto_now_add=True, blank=True)
    profile_updated = models.DateTimeField(auto_now=True, blank=True)


    def full_name(self):
        return '{}'.format(self.profile_user.first_name + " " + self.profile_user.last_name)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.full_name()
    

class Car(models.Model):
    """
    Taking down the car features all to be filled by the user who registers

    """
    OPTIONS = (
        ('n/a', 'N/A'),
        ('optional','Optional'),
        ('standard', 'Standard')
    )

    TRANSMISIION = (
        ('automatic', 'Automatic'),
        ('manual', 'Manual')
    )

    AUTO = (
        ('yes', 'Yes'),
        ('no', 'No')
    )


    FUEL = (
        ('diesel', 'Diesel'),
        ('pms', 'PMS')
    )


    AIRBAGS = (
        ('available', 'Available'),
        ('n/a', 'N/A')
    )

    ADS = (
        ('premium', 'Premium'),
        ('vip', 'VIP'),
        ('regular', 'Regular')
    )

    #Basic Features
    car_name = models.CharField(verbose_name="Car Name", max_length=200)
    car_price = models.PositiveIntegerField(blank=False, null=False)
    image = models.ImageField(verbose_name='Car Image Side', upload_to='listing/')
    car_front = models.ImageField(verbose_name='Car Image front', upload_to='media/', blank=True, null=True)
    car_back = models.ImageField(verbose_name='Car Image back', upload_to='media/', blank=True, null=True)
    car_interior = models.ImageField(verbose_name='Car Image Interior', upload_to='media/', blank=True, null=True)
    car_motion = models.ImageField(verbose_name='Car Image in Motion', upload_to='media/', blank=True, null=True)
    car_desc = models.CharField(max_length=1000, default=car_name)
    car_make = models.CharField(verbose_name="Car Maker", max_length=200)
    car_year = models.PositiveIntegerField(blank=True, null=True)
    car_width = models.PositiveIntegerField(blank=True, null=True)
    car_height = models.PositiveIntegerField(blank=True, null=True)
    car_length = models.PositiveIntegerField(blank=True, null=True)
    car_wheel_base = models.PositiveIntegerField(blank=True, null=True)
    car_mileage = models.PositiveIntegerField(blank=True, null=True)
    car_transmission = models.CharField(choices=TRANSMISIION, default='automatic', max_length=100)
    #Mechanical features
    car_cargo_capacity_space = models.PositiveIntegerField(blank=True, null=True)
    car_base_engine = models.PositiveIntegerField(blank=True, null=True)
    car_cylinders = models.CharField(max_length=50)
    car_fuel_capacity = models.PositiveIntegerField(blank=True, null=True)
    car_fuel_type = models.CharField(max_length=50)
    car_fuel_ecnonomy = models.CharField(max_length=50)
    car_horsepower_hp = models.PositiveIntegerField(blank=True, null=True)
    car_horsepower_rpm = models.PositiveIntegerField(blank=True, null=True)
    #Exterior/Interior Features
    car_season_tires = models.CharField(choices=OPTIONS, default='N/A', max_length=100)
    car_power_glass_sunroof = models.CharField(choices=OPTIONS, default='Automatic', max_length=100)
    car_tire_size = models.CharField(max_length=50)
    car_ac_climate_control = models.CharField(choices=OPTIONS, default='automatic', max_length=100)
    car_built_hard_drive = models.CharField(choices=AUTO, default='Yes', max_length=100)
    car_hd_radio = models.CharField(choices=OPTIONS, default='automatic', max_length=100)
    car_seats = models.CharField(choices=OPTIONS, default='automatic', max_length=100)
    car_offer = models.BooleanField(default=False)
    car_status = models.BooleanField(default=False)
    car_ads = models.CharField(choices=ADS, default='Regular', max_length=100)
    car_promoted = models.CharField(choices=AUTO, default='No', max_length=100)

    #User WHo posted the car
    car_user = models.ForeignKey(User, default=0, related_name='owner', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)

    # def get_absolute_image(self):
    #     return os.path.join('/media', self.image)


    def __str__(self):
        return self.car_name
    
    class Meta:
        ordering = ('-id',)


class Review(models.Model):
    
    review_title = models.CharField(verbose_name='Title', max_length=260)
    reviewer_name = models.CharField(verbose_name='Name', max_length=260)
    time_of_post = models.DateTimeField(auto_now_add=True, blank=True)
    time_updated = models.DateTimeField(auto_now=True, blank=True)
    car_reviewed = models.ForeignKey(Car, related_name='cars', on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    review = models.TextField()

    def __str__(self):
        return self.review_title


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )

    customer = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Car,null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(null=True, max_length=200, choices=STATUS)

    def orderCount(self):
        return self.product.count

    def __str__(self):
        return self.product.car_name

class Address(models.Model):
    COUNTRY= (
        ('nigeria', 'Nigeria'),
        ('africa','Africa'),
        ('south-america', 'South-America'),
        ('asia','Asia'),
        ('australasia', 'Australasia'),
        ('atlantica', 'Atlantica'),
        ('europe', 'Europe'),
        ('north-america', 'North-America')
    )

    customer = models.ForeignKey(User,null=True, related_name='customer', on_delete=models.CASCADE)
    profile_address = models.TextField(verbose_name='Address', blank=True, null=True)
    profile_country = models.CharField(choices=COUNTRY, default='Nigeria', max_length=100, blank=True, null=True)
    

    def full_add(self):
        return ('{} {}').format(self.profile_address, self.profile_country)
    
    def __str__(self):
        return self.customer.username
    



