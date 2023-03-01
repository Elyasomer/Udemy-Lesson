from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserField(UserAdmin):
    fieldsets = (
    (None, {'fields': ('name','surname','username','email','user_img','phone','password','is_superuser','is_staff','is_active','date_joined')}),
)

admin.site.register(User, UserField)
