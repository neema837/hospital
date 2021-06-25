from django.contrib import admin
from .models import Department, Doctor, Booking


# Register your models here.


# Register your models here.

class Dept_Admin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Department, Dept_Admin)


class Doc_Admin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Doctor, Doc_Admin)


class B_Admin(admin.ModelAdmin):
    list_display = ['name', 'created']


admin.site.register(Booking, B_Admin)
