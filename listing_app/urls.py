'''
    This is the views that links us to the main views.
'''
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'listing_app'


urlpatterns= [
    url(r"^home/", views.index, name='home'),
    url(r"^list/$", views.car_view, name='cars_list'),
    url(r"^grid/$", views.car_grid, name='cars_grid'),
    url(r"^list-page/$", views.car_page, name='cars_page'),
    url(r"^grid-page/$", views.car_page_grid, name='cars_page_grid'),
    url(r"^list-price/$", views.car_price_list, name='cars_price_list'),
    url(r"^grid-price/$", views.car_price_grid, name='cars_price_grid'),
    path('car_detail/<int:car_id>/', views.car_detailed, name='detail'),
    # path('car_detail/review/<int:car_id>/', views.review, name='detail')
    path("edit/<int:user_id>/", views.edit_dash, name="edit"),
    path("order/<int:user_id>", views.createOrder, name="create_order"),
    path("update_order/<str:pk>", views.updateOrder, name="update_order"),
    path("delete_order/<int:pk>", views.deleteOrder, name="delete_order"),
    path("order-page/<int:user_id>", views.orderPage, name="order_page"),
    path("register/", views.register, name="register"),
    path("dealer_register/", views.registerDealers, name="dealer_reg"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("contact/", views.contact_us, name="contact-us"),
    path("about-us/", views.about_us, name="about-us"),
    path("compare/", views.compareCar, name="compare"),
    # path("blog/", views.blog, name="blog"),
    path("blog-detail/", views.blog_detail, name="blog-detail"),
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)