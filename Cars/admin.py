from django.contrib import admin
from .models import NewCar,UsedCar
# Register your models here.
admin.site.register(NewCar)
admin.site.register(UsedCar)