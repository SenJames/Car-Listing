from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth, Group
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .import models
from .models import Car, UserProfile, Review, Address, Order, ContactUs
from .filters import CarFilter, CarIndexFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import OrderForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from dashboard_app.decorators import unauthenticated_user, dash_allowed_admin, allowed_users, dash_allowed_customer

# Create your views here.

# #This is the view for index
# class IndexView(TemplateView):
#     template_name = "listing_app/index.html"


def index(request):
    car_list = Car.objects.all().order_by('id')

    # creating the paginator
    paginator = Paginator(car_list, 2)  # Show 2 contacts per page.

    page_number = request.GET.get('page')

    try:
        lists = paginator.get_page(page_number)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)

    myFilter = CarIndexFilter(request.GET, queryset=car_list)
    car_list = myFilter.qs
    args = {
        'car_grids': car_list,
        'myFilter': myFilter,
        'lists': lists
    }

    return render(request, 'listing_app/index.html', args)


# This is the view for car_list main page
def car_view(request):
    car_list = Car.objects.all().order_by('id')

    # creating the paginator
    paginator = Paginator(car_list, 2)  # Show 25 contacts per page.

    page_number = request.GET.get('page')

    try:
        lists = paginator.page(page_number)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)

    myFilter = CarFilter(request.GET, queryset=car_list)
    car_list = myFilter.qs
    args = {
        'cars': car_list,
        'myFilter': myFilter,
        'lists': lists

    }
    return render(request, 'listing_app/car_list.html', args)

# This is the view for car_grid style


def car_grid(request):
    car_list = Car.objects.all().order_by('id')

    # creating the paginator
    paginator = Paginator(car_list, 2)  # Show 25 contacts per page.

    page_number = request.GET.get('page')

    try:
        lists = paginator.page(page_number)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)

    myFilter = CarFilter(request.GET, queryset=car_list)
    car_list = myFilter.qs
    args = {
        'car_grids': car_list,
        'myFilter': myFilter,
        'lists': lists
    }

    return render(request, 'listing_app/car_grid.html', args)

# This is the view for car_page_list style arrangd by name


def car_page(request):
    car_list = Car.objects.order_by('car_name')

    # creating the paginator
    paginator = Paginator(car_list, 2)  # Show 25 contacts per page.

    page_number = request.GET.get('page')

    try:
        lists = paginator.page(page_number)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)

    myFilter = CarFilter(request.GET, queryset=car_list)
    car_list = myFilter.qs
    args = {
        'page_list': car_list,
        'myFilter': myFilter,
        'lists': lists
    }

    return render(request, 'listing_app/car_page_list.html', args)


# This is the view for car_page_grid arranged by name
def car_page_grid(request):
    car_list = Car.objects.order_by('car_name')

    # creating the paginator
    paginator = Paginator(car_list, 2)  # Show 25 contacts per page.

    page_number = request.GET.get('page')

    try:
        lists = paginator.page(page_number)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)

    myFilter = CarFilter(request.GET, queryset=car_list)
    car_list = myFilter.qs
    args = {
        'grid': car_list,
        'myFilter': myFilter,
        'lists': lists
    }

    return render(request, 'listing_app/car_page_grid.html', args)


# This is the view for car_page_grid arranged by name
def car_price_grid(request):
    car_list = Car.objects.order_by('car_price')

    # creating the paginator
    paginator = Paginator(car_list, 2)  # Show 25 contacts per page.

    page_number = request.GET.get('page')

    try:
        lists = paginator.page(page_number)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)

    myFilter = CarFilter(request.GET, queryset=car_list)
    car_list = myFilter.qs
    args = {
        'price_grid': car_list,
        'myFilter': myFilter,
        'lists': lists
    }

    return render(request, 'listing_app/car_page_grid.html', args)


def car_price_list(request):
    car_list = Car.objects.order_by('car_price')

    # creating the paginator
    paginator = Paginator(car_list, 2)  # Show 25 contacts per page.

    page_number = request.GET.get('page')

    try:
        lists = paginator.page(page_number)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)

    myFilter = CarFilter(request.GET, queryset=car_list)
    car_list = myFilter.qs
    args = {
        'price_list': car_list,
        'myFilter': myFilter,
        'lists': lists

    }

    return render(request, 'listing_app/car_page_list.html', args)


# This is the view for car_detail
def car_detailed(request, car_id):
    car_details = Car.objects.get(id=car_id)
    car_reviews = Review.objects.filter(car_reviewed__id=car_id).count()

    if request.method == 'POST':
        author = request.POST['author']
        email = request.POST['email']
        comment = request.POST['comment']
        title = request.POST['title']

        obj_reviewed = Car.objects.get(id=car_id)

        reviewer = Review.objects.create(
            review_title=title, reviewer_name=author, email=email, review=comment, car_reviewed=obj_reviewed)
        reviewer.save()
        messages.success(request, 'Successful')
    else:
        print('Please check error as it wasnt successful')

    args = {
        'car_details': car_details,
        'car_reviews': car_reviews

    }

    return render(request, 'listing_app/car_detail.html', args)

# This is the review for the car


def review(request, car_id):

    if request.method == 'POST':
        author = request.POST['author']
        email = request.POST['email']
        comment = request.POST['comment']
        title = request.POST['title']

        obj_reviewed = Car.objects.get(id=car_id)

        reviewer = Review.objects.create(
            review_title=title, reviewer_name=author, email=email, review=comment, car_reviewed=obj_reviewed)
        reviewer.save()
        messages.success('Successful')
    else:
        print('Please check error as it wasnt successful')

    return redirect('listing_app/car_detail.html')

# This is the registration page for regular customers


@unauthenticated_user
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_pass = request.POST['confirm']

        if password == confirm_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken, Please try again')
                return redirect('listing_app:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists, contact admin')
                return redirect('listing_app:register')
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                user.save()
                group = Group.objects.get(name="customers")
                user.groups.add(group)
                user_prof = UserProfile.objects.create(profile_user=user)
                user_prof.profile_pic = 'listing_app/member1.png'
                # user.save()
                # user.save()
                user_prof.save()
                user.save()
                messages.success(
                    request, 'You have successfully registered, Please login')
                return redirect('listing_app:login')
        else:
            messages.error(request, 'Password mismatch')
            return redirect('listing_app:register')
    return render(request, 'listing_app/register.html')

# registeration for dealers


@unauthenticated_user
def registerDealers(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_pass = request.POST['confirm']

        if password == confirm_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request, f'{username} Taken, Please try again')
                return redirect('listing_app:dealer_reg')
            elif User.objects.filter(email=email).exists():
                messages.info(
                    request, f'{email} already exists, contact admin')
                return redirect('listing_app:dealer_reg')
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                user.save()
                group = Group.objects.get(name="dealers")
                user.groups.add(group)
                user_prof = UserProfile.objects.create(profile_user=user)
                user_prof.profile_pic = 'listing_app/member1.png'
                # user.save()
                # user.save()
                user_prof.save()
                user.save()
                messages.success(
                    request, 'You have successfully registered, Please login')
                return redirect('listing_app:login')
        else:
            messages.error(request, 'Password mismatch')
            return redirect('listing_app:register')
    return render(request, 'listing_app/reg_dealer.html')


# this is the login page
@unauthenticated_user
# @dash_allowed_users(allowed_roles=["dealers"])
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("cadmin")
        else:
            messages.info(request, 'invalid credentials')
            return redirect("listing_app:login")
    return render(request, 'listing_app/login.html')

# this is the logout page


def logout(request):
    auth.logout(request)
    messages.info(request, 'You have successfully logged out')
    return redirect('listing_app:login')

# this is the dashboard page


@login_required(login_url='listing_app/login.html')
# @allowed_users(allowed_roles=["customers"])
@dash_allowed_customer(allowed_roles=["customers"])
def dashboard(request):

    return render(request, 'listing_app/dashboard.html')

# edit Pages


@login_required(login_url='listing_app/login.html')
def edit_dash(request, user_id):
    return render(request, 'listing_app/edit.html')

# creatng the Order_form


@login_required(login_url='listing_app/login.html')
def createOrder(request, user_id):
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            author = form.save(commit=False)
            author.customer = request.user
            author.save()

            return redirect("cadmin")
        else:
            form = OrderForm(initial={'key': 'value'})
    context = {
        'form': form
    }

    return render(request, 'listing_app/order_form.html', context)

# This is for the update Order request


@login_required(login_url='listing_app/login.html')
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("cadmin")
        else:

            messages.error(request, 'Please fill all forms')
            form = OrderForm(initial={'key': 'value'})

    context = {
        'form': form,
    }
    return render(request, 'listing_app/order_form.html', context)

# This is for the Delete Order request


@login_required(login_url='listing_app/login.html')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == "POST":
        order.delete()
        return redirect("cadmin")

    context = {
        'item': order,
    }
    return render(request, 'listing_app/delete_form.html', context)


@login_required(login_url='listing_app/login.html')
def orderPage(request, user_id):
    order = Order.objects.filter(customer=user_id)
    order_count = Order.objects.filter(customer=user_id).count()

    context = {
        'order': order,
        'order_count': order_count
    }
    return render(request, 'listing_app/order_page.html', context)

# view for contact us


def contact_us(request):
    if request.method == "POST":
        email = request.POST['email']
        telephone = request.POST['telephone']
        comment = request.POST['comment']
        name = request.POST['name']
        if email != "" and comment != "" and name != "":
            comments = ContactUs.objects.create(
                email=email, name=name, phoneNo=telephone, comment=comment)
            comments.save()

            messages.success(request, 'Thank you. We would reach out shortly')
            return redirect('listing_app:contact-us')
        else:
            messages.error(request, 'Please fill in your details')
        # print(email, telephone, comment, name)
    return render(request, 'listing_app/contact-us.html')

# view for about us


def about_us(request):
    return render(request, 'listing_app/about-us.html')

# view for compare us


def compareCar(request):
    return render(request, 'listing_app/compare.html')


def blog_detail(request):
    context = {

    }
    return render(request, 'listing_app/blog-detail.html', context)
