from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, CustomAddress, Address, Country


class CustomAddressInline(admin.TabularInline):
    model = CustomAddress
    raw_id_fields = ['user']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_line_1', 'address_line_2', 'city', 'region', 'postal_code', 'country')
    list_filter = ('country',)
    search_fields = ('addressline_1', 'addressline_2', 'city', 'region', 'postal_code', 'country__name')


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email_address', 'phone_number', 'is_active', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email_address', 'phone_number', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email_address', 'phone_number', 'password1', 'password2'),
        }),
    )
    search_fields = ('email_address',)
    ordering = ('email_address',)


@admin.register(CustomAddress)
class CustomAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'is_default')
    list_filter = ('is_default', 'address__country')
    search_fields = (
        'user__email', 'address__addressline_1', 'address__addressline_2', 'address__city', 'address__region',
        'address__postal_code', 'address__country__name')


