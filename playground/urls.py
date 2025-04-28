from django.urls import path
from . import views

urlpatterns=[
    path('hello/',views.say_hello),
    path('nextpage/',views.xyz),
    path('register/', views.register_user,name='register'), 
    path('login/', views.login_user),
    path('products/', views.products,name='products'),  # Add this line
]