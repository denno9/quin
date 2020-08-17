from django.contrib import admin

# Register your models here.
from .models import (
    TheTeam,
    # TeamImage
    )
class TheTeamAdmin(admin.ModelAdmin):
    list_display = [
        # 'image',
        'fullname',
        # 'firstname',
        # 'middlename',   
        # 'lastname',
        'email',
        # 'description',
        'active'
    ]
    fieldsets = (
         ("ActiveUser", {
            'fields': (
                'active',
            ),
        }),
        ("Image", {
            'fields': (
                'image','image_tag',
            ),
        }),
        ("Details", {
            'fields': (
                'fullname','firstname','middlename','lastname',
            ),
        }),
         (None, {
            'fields': (
                'email',
                'description'
            ),
        }),
        

    )
    list_editable = ['active']
    readonly_fields =['image_tag']


fields = ['image_tag']
readonly_fields =['image_tag']

# admin.site.register(TeamImage)
admin.site.register(TheTeam,TheTeamAdmin)