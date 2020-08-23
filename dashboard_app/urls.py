"""Car_listing_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.urls import path, include
from dashboard_app import views
from dashboard_app.views import AdminPostView



app_name = 'dashboard_app'

urlpatterns = [
    # url(r'^dealer-admin', views.index, name='dashboard'),
    url(r'^$', views.home, name="dash_home"),
    path("tables/", views.tables, name="tables"),
    path("charts/", views.charts, name="charts"),
    path("my-profile/<str:pk>/", views.edit_profile, name="profile"),
    path("recover_pass/", views.recover_pass, name="pass_rec"),
    # path("view-blog/", AdminPostView.as_view(), name="view-blog"),
    path("view-blog/", views.view_blog, name="view-blog"),
    path("add-blog/", views.add_blog, name="add-blog"),
    path("edit-blog/<str:title>/", views.edit_blog, name="edit-blog"),  
    path("del-blog/<str:title>/", views.del_post, name="del-blog"),  
    path("add-prod/", views.add_prod, name="add-prod"),
    path("edit-prod/<str:pk>/", views.edit_prod, name="edit-prod"),
    path("view-prod/<str:pk>/", views.view_prod, name="view-prod"),
    path("del-prod/<str:pk>/", views.del_prod, name="del-prod"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)