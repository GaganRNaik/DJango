from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .producer import send_message

def send_stock_message(request,param):
    print(f"Received parameter: {param}")
    send_message(param)
    return JsonResponse({'status': 'Message sent for' + param})
