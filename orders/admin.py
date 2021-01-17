from django.contrib import admin
from .models import Service, Order, Imagescheme

admin.site.register(Service)
admin.site.register(Imagescheme)
admin.site.register(Order)

