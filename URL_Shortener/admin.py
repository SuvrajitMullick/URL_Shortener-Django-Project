from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(URL_Table)
admin.site.register(Country)
admin.site.register(Device)
