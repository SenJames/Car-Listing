# Generated by Django 3.0.3 on 2020-05-18 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=200, verbose_name='Car Name')),
                ('car_price', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='listing/', verbose_name='Car Image Side')),
                ('car_front', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Car Image front')),
                ('car_back', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Car Image back')),
                ('car_interior', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Car Image Interior')),
                ('car_motion', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Car Image in Motion')),
                ('car_desc', models.CharField(default=models.CharField(max_length=200, verbose_name='Car Name'), max_length=1000)),
                ('car_make', models.CharField(max_length=200, verbose_name='Car Maker')),
                ('car_year', models.PositiveIntegerField(blank=True, null=True)),
                ('car_width', models.PositiveIntegerField(blank=True, null=True)),
                ('car_height', models.PositiveIntegerField(blank=True, null=True)),
                ('car_length', models.PositiveIntegerField(blank=True, null=True)),
                ('car_wheel_base', models.PositiveIntegerField(blank=True, null=True)),
                ('car_mileage', models.PositiveIntegerField(blank=True, null=True)),
                ('car_transmission', models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], default='automatic', max_length=100)),
                ('car_cargo_capacity_space', models.PositiveIntegerField(blank=True, null=True)),
                ('car_base_engine', models.PositiveIntegerField(blank=True, null=True)),
                ('car_cylinders', models.CharField(max_length=50)),
                ('car_fuel_capacity', models.PositiveIntegerField(blank=True, null=True)),
                ('car_fuel_type', models.CharField(max_length=50)),
                ('car_fuel_ecnonomy', models.CharField(max_length=50)),
                ('car_horsepower_hp', models.PositiveIntegerField(blank=True, null=True)),
                ('car_horsepower_rpm', models.PositiveIntegerField(blank=True, null=True)),
                ('car_season_tires', models.CharField(choices=[('n/a', 'N/A'), ('optional', 'Optional'), ('standard', 'Standard')], default='N/A', max_length=100)),
                ('car_power_glass_sunroof', models.CharField(choices=[('n/a', 'N/A'), ('optional', 'Optional'), ('standard', 'Standard')], default='Automatic', max_length=100)),
                ('car_tire_size', models.CharField(max_length=50)),
                ('car_ac_climate_control', models.CharField(choices=[('n/a', 'N/A'), ('optional', 'Optional'), ('standard', 'Standard')], default='automatic', max_length=100)),
                ('car_built_hard_drive', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='Yes', max_length=100)),
                ('car_hd_radio', models.CharField(choices=[('n/a', 'N/A'), ('optional', 'Optional'), ('standard', 'Standard')], default='automatic', max_length=100)),
                ('car_seats', models.CharField(choices=[('n/a', 'N/A'), ('optional', 'Optional'), ('standard', 'Standard')], default='automatic', max_length=100)),
                ('car_offer', models.BooleanField(default=False)),
                ('car_status', models.BooleanField(default=False)),
                ('car_user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_age', models.PositiveIntegerField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('profile_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('profile_user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_title', models.CharField(max_length=260, verbose_name='Title')),
                ('reviewer_name', models.CharField(max_length=260, verbose_name='Name')),
                ('time_of_post', models.DateTimeField(auto_now_add=True)),
                ('time_updated', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254)),
                ('review', models.TextField()),
                ('car_reviewed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='listing_app.Car')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listing_app.Car')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('profile_country', models.CharField(blank=True, choices=[('nigeria', 'Nigeria'), ('africa', 'Africa'), ('south-america', 'South-America'), ('asia', 'Asia'), ('australasia', 'Australasia'), ('atlantica', 'Atlantica'), ('europe', 'Europe'), ('north-america', 'North-America')], default='Nigeria', max_length=100, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
