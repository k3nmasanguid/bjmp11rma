from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
User = get_user_model()
class UsersAdmin(BaseUserAdmin):
    list_display = ['email', 'date_joined','last_login','is_superuser','is_active','status']
    list_filter = ['is_active','status']
    readonly_fields = ('date_joined','last_login')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (None, {'fields': ('date_joined','last_login',)}),
        ('Permissions', {'fields': ('is_active','is_admin','is_staff','is_superuser','status','batch')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ['email']
    ordering = ['-date_joined']
    filter_horizontal = ()
    


admin.site.register(User, UsersAdmin)
