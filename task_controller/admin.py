from django.contrib import admin
from .models import Order, Task
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'images', 'created_time')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'time_counter', 'created_time')
    search_fields = ('name', 'order')