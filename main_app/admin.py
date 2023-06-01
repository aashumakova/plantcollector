from django.contrib import admin
from .models import Plant, Watering

# Register your models here.
from .models import Plant
admin.site.register(Plant)
admin.site.register(Watering)
