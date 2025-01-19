from django.contrib import admin
from .models import User,UserHoliday,Holiday,Country

from django.contrib import admin

# Register your models here.

admin.site.register(UserHoliday)
admin.site.register(Holiday)
admin.site.register(Country)
admin.site.register(User)

