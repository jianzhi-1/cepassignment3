from django.contrib import admin
from .models import Food, Restaurant, Rating

# Register your models here.

class FoodInline(admin.StackedInline):
    model = Food
    fields = ('name',)
    extra = 0
    
class RatingAdmin(admin.ModelAdmin):
    inlines = [FoodInline,]
    model = Rating
    
class RestaurantedFoodInline(admin.TabularInline):
    model = Food.restaurant.through
    extra = 0

class RestaurantAdmin(admin.ModelAdmin):
    inlines = [RestaurantedFoodInline,]
    model = Restaurant

admin.site.register(Food)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Rating, RatingAdmin)
