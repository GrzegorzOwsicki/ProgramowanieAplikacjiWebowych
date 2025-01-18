from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('test/',views.test,name='test'),
    path('getcountries/',views.getCountries,name='getcountries'),
]