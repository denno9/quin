from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Contact

User = get_user_model()
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'last_login',
         'active',
         'staff',
         'admin',
         'superuser'
    ]
    list_editable = ['active','admin','staff','superuser']

admin.site.register(User,UserAdmin)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'subject',
         'body',
         'date_added'
        
    ]
    date_hierarchy = 'date_added'
admin.site.register(Contact,ContactAdmin)