from django.contrib import admin
from product.models import CustomUser,Product,Cart,Renting,Wishlist,Payment
# Register your models here.
admin.site.register(CustomUser),
admin.site.register(Product),
admin.site.register(Cart),
admin.site.register(Renting),
admin.site.register(Wishlist),
admin.site.register(Payment),