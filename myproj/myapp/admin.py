from django.contrib import admin

# Register your models here.
from .models import Landlord
from .models import Housing
admin.site.register(Landlord)
admin.site.register(Housing)
