from django.contrib import admin
from .models import User, Address
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    fields = (
        'first_name',
        'last_name',
        'email',
    )
    list_display = [
        'first_name',
        'last_name',
        'email',
        'contact_number',
    ]

    search_fields = (
        'email', 'first_name',
    )


class AddressAdmin(admin.ModelAdmin):

    fields = (
        'user',
        'address_line_1',
        'address_line_2',
        'building_no',
        'floor_no',
        'house_no',
        'city',
        'state',
        'pin_code')

    list_display = [
        'user',
        'city',
        'state'
    ]
    search_fields = (
        'user', 'floor_no', 'house_no'
    )

admin.site.register(User, UserAdmin)
admin.site.register(Address, AddressAdmin)