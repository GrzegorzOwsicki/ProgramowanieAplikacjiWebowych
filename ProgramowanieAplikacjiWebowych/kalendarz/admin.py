from django.contrib import admin
from .models import User,UserHoliday,Holiday,Country
# Register your models here.



admin.site.register(User)
admin.site.register(UserHoliday)
admin.site.register(Holiday)
admin.site.register(Country)