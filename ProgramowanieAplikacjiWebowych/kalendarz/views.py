from django.shortcuts import render
from datetime import datetime
from .models import Holiday,Country,User
import requests, json
from django.http import JsonResponse,HttpResponse
# Create your views here.

def register(request):
    data = json.load(request.body.decode('utf-8'))
    user_name = data.get("username")
    mail = data.get("email")
    pass_word= data.get("password")
    countryy = data.get("country")
    
    if not User.objects.filter(email=mail).exists():
        if not User.objects.filter(username=user_name).exists():
            user_username = user_name
            user_email = mail
            user_password = pass_word
            user_country = Country.objects.get(code = countryy)
    
            user_obj, created = User.objects.create(
                username = user_username,
                email = user_email, 
                password = user_password,
                country = user_country
            )
           
            return JsonResponse({'id': user_obj.id}, status=200)
        else:
            return JsonResponse({'error': "Username already in use"}, status=409)
    else:
        return JsonResponse({'error': "Email already in use"}, status=409)

def login(request):
    #data = json.load(request.body.decode('utf-8'))
    #login = data.get("login")
    #pass_word= data.get("password")
    login = request.GET.get("login")
    pass_word= request.GET.get("password")

    if User.objects.filter(username=login).exists():
        if User.objects.filter(password=pass_word).exists():
                user = User.objects.filter(username=login).filter(password=pass_word).get()
                return JsonResponse({'id': user.id}, status=200)
        else:
            return JsonResponse({'error': "Incorect login or password"}, status=404)
    elif User.objects.filter(email=login).exists(): 
        if User.objects.filter(password=pass_word).exists():
            user = User.objects.filter(email=login).filter(password=pass_word).get()
            #return JsonResponse({'id': user.id}, status=200)
            return HttpResponse("done")
        else:
            return JsonResponse({'error': "Incorect login or password"}, status=404)
    else:
        return JsonResponse({'error': "Incorect login or password"}, status=404)