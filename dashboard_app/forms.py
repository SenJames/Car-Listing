from django import forms
from listing_app.models import *
from blog.models import Post, Category, Author, Comment
from listing_app.models import UserProfile
from django.forms import ModelForm
from  django.contrib.auth.models import User, auth
from django.core import validators


################Options for ProfileForm##################
SELLER = (
    ('dealer', 'Dealer'),
    ('private','Private'),
)

###############Options for Car Product#############################
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
###############################

class UserForm(ModelForm):
    botcatcher = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'form-control'}),required=False, validators=[validators.MaxLengthValidator(0)]),
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email','username' )
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UserProfileForm(ModelForm):
    profile_pic = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    profile_seller = forms.CharField(label='Dealer/Seller', widget=forms.Select(choices=SELLER, attrs={'class': 'form-control'}), max_length=10)
    profile_phone = forms.CharField(label='Contact No:', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=14),

    class Meta:
        model = UserProfile

        exclude = ('profile_user',)


#Creating the Product

class CarForm(ModelForm):
    car_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=200)
    car_price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    car_front = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    car_back = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    car_interior = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    car_motion = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    car_desc = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control'}),)
    car_make = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=200)
    car_year = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    car_width = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    car_height = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    car_length = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    car_wheel_base = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    car_mileage = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    car_transmission = forms.CharField(widget=forms.Select(choices=TRANSMISIION, attrs={'class': 'form-control'}))

    #Mechanical features
    car_cargo_capacity_space = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    car_base_engine = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    car_cylinders = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=50)
    car_fuel_capacity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    car_fuel_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=50)
    car_fuel_ecnonomy = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=50)
    car_horsepower_hp = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    car_horsepower_rpm = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    #Exterior/Interior Features
    car_season_tires = forms.CharField(widget=forms.Select(choices=OPTIONS, attrs={'class': 'form-control'}))
    car_power_glass_sunroof = forms.CharField(widget=forms.Select(choices=OPTIONS, attrs={'class': 'form-control'}))
    car_tire_size = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=50)
    car_ac_climate_control = forms.CharField(widget=forms.Select(choices=OPTIONS, attrs={'class': 'form-control'}))
    car_built_hard_drive = forms.CharField(widget=forms.Select(choices=AUTO,attrs={'class': 'form-control'}))
    car_hd_radio = forms.CharField(widget=forms.Select(choices=OPTIONS, attrs={'class': 'form-control'}))
    car_seats = forms.CharField(widget=forms.Select(choices=OPTIONS, attrs={'class': 'form-control'}))
    car_offer = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    car_status = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    car_ads = forms.CharField(widget=forms.Select(choices=ADS, attrs={'class': 'form-control'}))
    car_promoted = forms.CharField(widget=forms.Select(choices=AUTO, attrs={'class': 'form-control'}), max_length=10, required=False)
    class Meta:
        model = Car
        fields = '__all__'
        exclude = ('car_user',)

class AuthorForm(forms.ModelForm):
    author = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=50)
    class Meta:
        model = Author
        fields = ("author",)


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("pst_title","content", "category", "user","pst_img",)

class CategoryForm(forms.ModelForm):
    cat_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    desc = models.TextField(blank=True, null=True, verbose_name='Description')
    class Meta:
        model = Category
        fields = ("cat_name","desc",)

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("name","email","comment", "post",)











#         widgets = {
#             # 'profile_pic': forms.ImageField(widget=forms.ClearableFileInput()),
#             # 'profile_phone': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=14),
#             # 'profile_seller': forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}), max_length=10),
            
#         }

# #         field_classes = {'precio': forms.CharField}
# # widgets = {'precio': forms.NumberInput}

    
