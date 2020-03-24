from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Review)

admin.site.site_header = "Yuri Hacks"