from django.contrib import admin
# Register your models here.


from .models import UserProfile,CartItem

admin.site.register(UserProfile)
admin.site.register(CartItem)
