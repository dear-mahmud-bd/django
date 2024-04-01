from django.contrib import admin
from .models import UserBankAccount, UserAddress

# Register your models here.
class UserBankAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_type', 'account_no', 'balance')
    list_filter = ('account_type',)
    search_fields = ('user__username', 'account_no')
admin.site.register(UserBankAccount, UserBankAccountAdmin)

class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_email', 'street_address', 'postal_code', 'city', 'country')  # Include 'user_email' here
    search_fields = ('user__username', 'user__email')  # Add 'user__email' here
    def user_email(self, obj):
        return obj.user.email  # Define a function to return the user's email
    user_email.short_description = 'User Email'  # Set the short description for the user email column

admin.site.register(UserAddress, UserAddressAdmin)
