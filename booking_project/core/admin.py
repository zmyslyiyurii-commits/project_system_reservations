from django.contrib import admin
from .models import Room, Booking

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    # Відображення полів у списку (Пункт 6 ТЗ)
    list_display = ('name', 'room_type', 'capacity', 'price_per_day')
    list_filter = ('room_type',)
    search_fields = ('name',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # Керування бронюваннями 
    list_display = ('room', 'user', 'start_date', 'end_date', 'created_at')
    list_filter = ('start_date', 'room')
    # Можливість редагування та видалення вже вбудована в Django Admin