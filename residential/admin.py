from django.contrib import admin
from .models import Flat, Photo

# main tables
admin.site.register(Flat)
admin.site.register(Photo)
