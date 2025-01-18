from django.shortcuts import render
from datetime import datetime
from .models import Holiday,Country,User
import requests, json
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.core.serializers import serialize
from django.contrib.auth import login as authLogin
# Create your views here.

def register(request):
    print("test")
    data = json.loads(request.body.decode('utf-8'))
    user_name = data.get("username")
    mail = data.get("email")
    pass_word= data.get("password")
    countryy = data.get("country")

    error = {'username_in_use':False,'email_in_use':False}
    success = True
    if User.objects.filter(email=mail).exists():
        error['username_in_use'] = True
        success = False
    if User.objects.filter(email=mail).exists():
        error['email_in_use'] = True
        success = False
    
    if success:
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
        return JsonResponse(error, status=409)

def login(request):
    data = json.loads(request.body.decode('utf-8'))
    login = data.get("login")
    pass_word= data.get("password")

    if User.objects.filter(username=login).filter(password=pass_word).exists().exists():
        user = User.objects.filter(username=login).filter(password=pass_word).get()

        return JsonResponse({'id': user.id}, status=200)
    
    elif User.objects.filter(email=login).filter(password=pass_word).exists(): 
        user = User.objects.filter(email=login).filter(password=pass_word).get()
        return JsonResponse({'id': user.id}, status=200)
    
    else:
        return JsonResponse({'error': "Incorect login or password"}, status=404)
    
def test(request):
    return render(request,'home.html')

def getCountries(request):
    countries = Country.objects.values('country', 'code')
    countries = list(countries) 
    print(countries) 
    return JsonResponse(countries, safe=False, status=200)
