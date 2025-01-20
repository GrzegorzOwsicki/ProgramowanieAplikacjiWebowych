from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('home/',views.home,name='home'),
    path('monthHolidays/',views.getMonthlyHolidays,name='monthHolidays'),
    path('getUserHolidays/',views.getUserHolidays,name="getUserHolidays"),
    path('addUserHoliday/',views.addUserHoliday,name="addUserHoliday"),
    path('getcountries/',views.getCountries,name='getcountries'),
    path('deleteUserHoliday/',views.deleteUserHoliday,name="deleteUserHoliday"),
    path('redirectLogin/',views.redirectLogin,name='redirectLogin'),
    path('redirectRegister/',views.redirectRegister,name='redirectRegister'),
]