from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Product,Category,Cart,CartItem,Review,ProductRating,Wishlist,Order,OrderItem
# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name")
admin.site.register(CustomUser, CustomUserAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "featured"]

admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]

admin.site.register(Category, CategoryAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ("cart_code",)
admin.site.register(Cart, CartAdmin)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "product", "quantity")
admin.site.register(CartItem, CartItemAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["product", "rating", "review", 'created', "updated"]
admin.site.register(Review, ReviewAdmin)


class WishlistAdmin(admin.ModelAdmin):
    list_display = ("user", "product")
admin.site.register(Wishlist, WishlistAdmin)


admin.site.register(Order)
admin.site.register(OrderItem)


