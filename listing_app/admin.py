from django.contrib import admin
from django.contrib.auth.models import User
from listing_app.models import UserProfile, Car, Review, Order, Address, ContactUs
# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ("car_name", "car_price",)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("reviewer_name", "time_of_post", "car_reviewed")


class OrderAdmin(admin.ModelAdmin):
    list_display = ("date_created", "customer")


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("profile_user",)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Address)
admin.site.register(ContactUs)
