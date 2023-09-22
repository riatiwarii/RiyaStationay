# appname/urls.py

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('logout/', views.user_logout, name="logout"),
    path('new/',views.register,name='registration_form'),
    path('login/',views.user_login,name='login'),
    path("cart/", views.cart, name="cart"),
    path("add_to_cart/", views.add_to_cart, name="add_to_cart"),
    path("remove_from_cart/<str:item_id>/", views.remove_from_cart, name="remove_from_cart"),
]

