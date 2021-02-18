from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account
# Register your models here.


class AccountAdmin(UserAdmin):
    # Attributes of columns to be displayed in Admin panel
    list_display = ('email', 'username', 'date_join', 'last_login', 'is_admin', 'is_staff')
    # Create a search bar in admin console to search and will use email and username as search fields
    search_fields = ('email', 'username')
    # Fields that you can only read & can't be changed manually
    readonly_fields = ('date_join', 'last_login', )
    # Some required fields (keep it blank)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
