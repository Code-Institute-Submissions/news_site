from django.contrib import admin
from .models import Podcast
from .models import Purchase

admin.site.register(Podcast)
admin.site.register(Purchase)