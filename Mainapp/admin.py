from django.contrib import admin

# Register your models here.
from .models import topic

from.models import Entry

admin.site.register(topic)

admin.site.register(Entry)
