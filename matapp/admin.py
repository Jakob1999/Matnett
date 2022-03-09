from django.contrib import admin

# Register your models here.

from .models import *

admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Recipe)
