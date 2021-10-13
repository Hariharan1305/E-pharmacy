from django.contrib import admin
from .models import medicine,orderdetailsmodel
# Register your models here.

admin.site.register(orderdetailsmodel)
admin.site.register(medicine)
