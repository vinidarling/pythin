from django.contrib import admin
from myapp.models import student

# Register your models here.
class studentadmin(admin.ModelAdmin):
    i={'name','roll','marks','dob','email'}
admin.site.register(student,)

