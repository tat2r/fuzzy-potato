from django.contrib import admin

# Register your models here.

from import_export.admin import ImportExportModelAdmin 
from .models import (ModelName, Customer, Van, Rental, AdditionalDriver, AdobeDriver)

# admin.site.register(ModelName)
# admin.site.register(Customer)
# admin.site.register(Van)
# admin.site.register(Rental)
# admin.site.register(AdditionalDriver)
# admin.site.register(AdobeDriver)
@admin.register(ModelName, Customer, Van, Rental, AdditionalDriver, AdobeDriver)
class ViewAdmin(ImportExportModelAdmin):
	pass