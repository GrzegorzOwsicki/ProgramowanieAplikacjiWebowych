from django.shortcuts import render
from datetime import datetime
from .models import Holiday,Country,User,UserHoliday
import requests, json
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.core.serializers import serialize
from django.contrib.auth import login as authLogin
from django.contrib.auth import logout as authLogut
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        authLogut(request)
        data = json.loads(request.body.decode('utf-8'))
        user_name = data.get("username")
        mail = data.get("email")
        pass_word= data.get("password")
        country = data.get("country")

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
            user_country = Country.objects.get(code = country)

            user_obj, created = User.objects.get_or_create(
                username = user_username,
                email = user_email, 
                country = user_country
            )
            user_obj.set_password(user_password)
            user_obj.save()
            authLogin(request,user_obj,backend='kalendarz.backends.EmailOrUsernameAuthBackend')
            return JsonResponse({'redirect_url': '/'}, status=200)
        else:
            return JsonResponse(error, status=409)
    return JsonResponse({"error":"Method unallowed"},status = 405)

def login(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        login = data.get("login")
        pass_word= data.get("password")
        authLogut(request)
        user = authenticate(request,username=login,password=pass_word)
        print(user)
        if user == None:
            print("test")
            user = authenticate(request,email=login,password=pass_word)
        if user:
            #user = User.objects.filter(username=login).filter(password=pass_word).get()
            authLogin(request,user,backend='kalendarz.backends.EmailOrUsernameAuthBackend')
            return JsonResponse({'redirect_url': '/'}, status=200)
        
        elif user: 
            authLogin(request,user,backend='kalendarz.backends.EmailOrUsernameAuthBackend')
            return JsonResponse({'redirect_url': '/'}, status=200)
        
        else:
            return JsonResponse({'error': "Incorect login or password"}, status=404)
    return JsonResponse({"error":"Method unallowed"},status = 405)

def logout(request):
    authLogut(request)
    return render(request,'home.html')

def home(request):
    return render(request,'home.html')

def redirectLogin(request):
    return render(request,'login.html')

def redirectRegister(request):
    return render(request,'register.html')

def getCountries(request):
    countries = Country.objects.values('country', 'code')
    countries = list(countries) 
    return JsonResponse(countries, safe=False, status=200)

@login_required
def getMonthlyHolidays(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        country = data.get('country')
        country = Country.objects.get(code = country)
        public = data.get('public')
        month = data.get('month')
        if country == None:
            user = request.user
            country = Country.objects.get(code = user.country)
        today = datetime.now()
        if public:
            dates = Holiday.objects.filter(date__year=today.year-1,date__month=month,country=country,public=public).values()
        else:
            dates = Holiday.objects.filter(date__year=today.year-1,date__month=month,country=country).values()
        dates = list(dates)
        return JsonResponse(dates,safe=False,status=200)
    return JsonResponse({"error":"Method unallowed"},status = 405)

@login_required
def getUserHolidays(request):
    user = request.user
    dates = UserHoliday.objects.filter(user=user).values()
    dates = list(dates)
    return JsonResponse(dates,safe=False,status=200)

@login_required
def addUserHoliday(request):
    if request.method == 'POST':
        user = request.user
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('name')
        date = data.get('date')
        newUserHoliday, craeated = UserHoliday.objects.get_or_create(
            user = user,
            name = name,
            date = date
        )
        return JsonResponse({"response":"done"},status=200)
    return JsonResponse({"error":"Method unallowed"},status = 405)

@login_required
def deleteUserHoliday(request):
    if request.method == 'POST':
        user = request.user
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('name')
        date = data.get('date')
        UserHoliday.objects.filter(user=user,name=name,date=date).delete()
        return(JsonResponse({"deleted":"yes"},status=200))
    return JsonResponse({"error":"Method unallowed"},status = 405)