from django.http import HttpResponse
from django.shortcuts import redirect


#UnAutthenitcate User decorator
def unauthenticated_user(view_func):
    """
    Redirects logged in user to dashboard
    """
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/customer-admin/")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


#This decorator checks for user permissions and assigns permission
def allowed_users(allowed_roles=[]):
    def decorators(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                print(group)
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse("You  are not authorized to view this page")
            print("Yeaaa this person: " + str(allowed_roles))
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorators

# def admin_only(view_func) for Dashboard
#This decorator checks for user permissions and assigns permission
def dash_allowed_admin(allowed_roles=[]):
    def decorators(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                print("group exists")
                group = request.user.groups.all()[0].name
                print(group)

                if group in allowed_roles and group == "dealers":
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect('cadmin')
            else:
                print("No group exists")
                return HttpResponse("There is no such group as this.")
            # return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorators



# def admin_only(view_func) for Customer Dashboard
#This decorator checks for user permissions and assigns permission
def dash_allowed_customer(allowed_roles=[]):
    def decorators(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                print("group exists")
                group = request.user.groups.all()[0].name
                print(group)

                if group in allowed_roles and group == "customers":
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect('dashboard_app:dash_home')
            else:
                print("No group exists")
                return HttpResponse("There is no such group as this.")
            # return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorators

