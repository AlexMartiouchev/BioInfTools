from django.contrib import admin

from .models import AvailablePrimers, UnavailablePrimers

admin.site.register(AvailablePrimers)
admin.site.register(UnavailablePrimers)
