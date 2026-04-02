from django.contrib import admin
from .models import Category, Room, Booking

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_per_hour', 'capacity')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'start_time', 'end_time', 'created_at')
    list_filter = ('start_time', 'room')