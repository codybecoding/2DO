from django.contrib import admin

# Register your models here.
from .models import UserTask

class UserTaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'pub_date', 'user')


admin.site.register(UserTask, UserTaskAdmin)
