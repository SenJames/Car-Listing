from django.shortcuts import render
from listing_app.models import *
from listing_app.models import UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from listing_app import views
from blog.models import Post, Category, Author, Comment
from dashboard_app.forms import UserForm, UserProfileForm, CarForm, CategoryForm, PostForm, AuthorForm, CommentForm
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .decorators import allowed_users, dash_allowed_admin  # , unauthenticated_dash
# Create your views here.


@login_required(login_url='/car-listing/login/')
@dash_allowed_admin(allowed_roles=["dealers"])
# @unauthenticated_dash(["dealer"])
def home(request):

    context = {

    }
    return render(request, 'dashboard_app/index.html', context)


@login_required(login_url='/car-listing/login/')
def recover_pass(request):

    context = {

    }
    return render(request, 'dashboard_app/forgot-password.html', context)

# Table for handling users, dealers and customers


@login_required(login_url='/car-listing/login/')
def tables(request):
    dealers_group = User.objects.filter(groups__name="dealers")
    # dealers_car_count = Car.objects.filter(car_user=dealers_group)
    customer_group = User.objects.filter(groups__name="customers")
    staff_group = User.objects.filter(is_superuser=True)
    cars_available = Car.objects.all()
    date_cars = Car.objects.last().date_added
    date_user = customer_group.last().date_joined
    date_dealer = dealers_group.last().date_joined
    # print(date_cars.date_added)
    print(date_user)
    print(staff_group)
    print(date_user)
    print(date_dealer)
    context = {
        "dealers": dealers_group,
        "customers": customer_group,
        "staff": staff_group,
        "products": cars_available,
        "lastAdded_cars": date_cars,
        "lastAdded_customer": date_user,
        "lastUpdated_dealer": date_dealer,

    }
    return render(request, 'dashboard_app/tables.html', context)


@login_required(login_url='/car-listing/login/')
def charts(request):

    context = {

    }
    return render(request, 'dashboard_app/charts.html', context)


@login_required(login_url='/car-listing/login/')
@allowed_users(allowed_roles=["dealers"])
def view_blog(request):
    blog = Post.objects.all()

    if request.method == 'POST':
        catName = request.POST.get('catName')
        catDesc = request.POST.get('catDesc')
        print(catDesc)
        print(catName)

        try:

            cat = Category.objects.get(cat_name=catName.upper())
            messages.info(request, 'The category exits')
            return redirect("/dashboard/view-blog/")

        except Category.DoesNotExist:
            cat = Category.objects.create(
                cat_name=catName.upper(), desc=catDesc.upper())
            cat.save()
            messages.success(request, 'Category updated')
            return redirect("/dashboard/view-blog/")
    context = {
        'blog': blog
    }
    return render(request, 'dashboard_app/view-blog.html', context)


@login_required(login_url='/car-listing/login/')
@dash_allowed_admin(allowed_roles=["dealers"])
# @allowed_users(allowed_roles=["admin", "staff"])
def add_blog(request):
    # form = PostForm()
    categories = Category.objects.all()
    user = request.user

    if request.method == 'POST':
        print(request.POST)
        title = request.POST.get('title')
        author = request.user
        content = request.POST.get('content')
        image = request.FILES.get('image')
        category = request.POST.get('category')

        try:
            blog = Post.objects.filter(pst_title=title)
            if blog.exists():
                messages.error(request, 'A blog with this title exists')
                return redirect("/dashboard/add-blog/")
            else:

                post = Post.objects.create(
                    pst_title=title, pst_img=image, content=content, user=author)
                post.save()
                cate = Category.objects.get(cat_name=category)
                post.category.add(cate)
                post.save()
                messages.success(request, 'New Blog Uploaded')
                return redirect("dashboard_app:view-blog")
        except Exception as e:
            messages.error(request, f'{str(e)}')
            return redirect("/dashboard/add-blog/")
    context = {
        'categories': categories,
        'user': user
    }
    return render(request, 'dashboard_app/add-blog.html', context)


@login_required(login_url='/car-listing/login/')
# @allowed_users(allowed_roles=["admin", "staff"])
@dash_allowed_admin(allowed_roles=["dealers"])
def edit_blog(request, title):
    eachBlog = Post.objects.get(pst_title=title)
    form = PostForm(instance=eachBlog)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES or None, instance=eachBlog)
        try:
            if form.is_valid():
                form.save()
                messages.info(request, 'Successfully Updated')

                return redirect("dashboard_app:view-blog")
            else:
                messages.error(request, 'Please enter the right values')
                return redirect("/dashboard/edit-blog/" + "{}".format(title))
        except Exception as e:
            messages.error(request, f'{str(e)}')
            return redirect("/dashboard/edit-blog/" + "{}".format(title))

    context = {
        "eachBlog": eachBlog,
        "form": form,

    }
    return render(request, 'dashboard_app/edit-blog.html', context)


@login_required(login_url='/car-listing/login/')
@dash_allowed_admin(allowed_roles=["dealers"])
# @allowed_users(allowed_roles=["admin", "staff"])
def del_post(request, title):
    user = request.user
    post = Post.objects.get(pst_title=title)
    print(post)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Item Successfully Deleted')
        return redirect('/dashboard/view-blog/')
    else:
        messages.error(request, 'Unable to Delete Iteam')
        return redirect('/dashboard/view-blog/')

    return render(request, 'dashboard_app/view-blog.html')


@login_required(login_url='/car-listing/login/')
# @allowed_users(allowed_roles=["admin", "staff"])
@dash_allowed_admin(allowed_roles=["dealers"])
def edit_prod(request, pk):
    product = Car.objects.get(id=pk)
    form = CarForm(instance=product)

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES or None, instance=product)
        if form.is_valid():
            form.save()
            return redirect("dashboard_app:dash_home")
        else:
            return messages.error(request, 'Please fill all forms')

    context = {
        'form': form,
    }
    return render(request, 'dashboard_app/edit-product.html', context)


@login_required(login_url='/car-listing/login/')
# @allowed_users(allowed_roles=["admin", "staff"])
def view_prod(request, pk):
    cars = Car.objects.filter(car_user__id=pk)

    context = {
        'cars': cars
    }
    return render(request, 'dashboard_app/view-product.html', context)


@login_required(login_url='/car-listing/login/')
# @allowed_users(allowed_roles=["admin", "staff"])
def add_prod(request):

    form = CarForm()

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES or None)
        if form.is_valid():
            author = form.save(commit=False)
            author.car_user = request.user
            author.save()
            return redirect("dashboard_app:dash_home")
        else:
            messages.error(request, 'There is an error with the form')
            return redirect("dashboard_app:add-prod")
    context = {
        'form': form
    }
    return render(request, 'dashboard_app/add-product.html', context)


@login_required(login_url='/car-listing/login/')
# @allowed_users(allowed_roles=["admin", "staff"])
def del_prod(request, pk):
    cars = Car.objects.filter(id=pk)

    if request.method == 'POST':
        cars.delete()
        return redirect('dashboard_app:dash_home')
    else:
        return redirect("dashboard_app:dash_home")

    context = {
        'cars': cars
    }
    return render(request, 'dashboard_app/view-product.html', context)

#######################################################################
# Edit The Profiel


@login_required(login_url='/car-listing/login/')
def edit_profile(request, pk):
    user = User.objects.get(id=pk)
    try:
        profile = UserProfile.objects.get(profile_user__id=pk)
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(profile_user=user)
        profile.profile_pic = 'listing_app/member1.png'
        profile.save()

    form = UserForm(instance=user)
    proform = UserProfileForm(instance=profile)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        proform = UserProfileForm(
            request.POST or None, request.FILES or None, instance=profile)
        if form.is_valid and proform.is_valid:
            form.save()
            proform.save()
            return redirect("dashboard_app:dash_home")
        else:
            return messages.error(request, 'Please fill all forms')

    context = {
        'form': form,
        'proform': proform
    }
    return render(request, 'dashboard_app/profile.html', context)


# Adding the Blog Feature with Class Based View Method

class AdminPostView(ListView):
    form_class = PostForm
    model = Post
    context_object_name = "post_list"
    initial = {'key': 'value'}
    template_name = "dashboard_app/view-blog.html"

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     most_recent = Post.objects.order_by('-created_date')
    #     return most_recent

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # most_recent = Post.objects.order_by('-created_date')
    #     context['most_recent'] = self.most_recent
    #     return context

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(initial=self.initial)
    #     return render(request, self.template_name, {'form': form})

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         return HttpResponseRedirect('/dasboard/view-blog/')
    #     return render(request, self.template_name, {'form': form})
