from django.contrib import admin
from .models import Flight
from .models import Review

# Register your models here.

admin.site.register(Flight)
admin.site.register(Review)