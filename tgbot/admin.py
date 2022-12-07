from django.contrib import admin

from .models import User, Category, Subcategory, Brand, Ad


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Brand)
admin.site.register(Ad)