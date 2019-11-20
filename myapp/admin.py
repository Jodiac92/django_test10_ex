from django.contrib import admin
from myapp.models import Gogek

# Register your models here.
class GogekAdmin(admin.ModelAdmin):
    list_display = ('gogek_name','gogek_tel')
    
admin.site.register(Gogek, GogekAdmin)