'''
    This is the views that links us to the main views.
'''
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from blog import views

app_name = 'blog'

urlpatterns= [
    # path("blog-post/", PostListView.as_view(), name='posts'),
    path("blog-post/", views.Postlist, name='posts'),
    path("blog-detail/<str:pk>", PostDetailView.as_view(), name="post-det")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)