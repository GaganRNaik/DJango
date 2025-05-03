from django.urls import path
from .views import send_stock_message

urlpatterns = [
    path('send/<str:param>/', send_stock_message),
]
    