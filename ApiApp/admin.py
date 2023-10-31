from django.contrib import admin

# Register your models here.
from .models import Category,ECommerce,Company
admin.site.register(Category)
admin.site.register(ECommerce)
admin.site.register(Company)
