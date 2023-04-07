from django.contrib import admin
from .models import PlantType, Plant, Garden

# Register your models here.


admin.site.register(PlantType)
admin.site.register(Plant)
admin.site.register(Garden)
