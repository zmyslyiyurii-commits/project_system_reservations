from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Room(models.Model):
    ROOM_TYPES = [
        ('conf', 'Конференц-зал'),
        ('office', 'Офіс'),
        ('meet', 'Кімната для зустрічей'),
    ]
    name = models.CharField(max_length=100, verbose_name="Назва кімнати")
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES, verbose_name="Тип")
    capacity = models.IntegerField(verbose_name="Вмістимість (осіб)")
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна за добу")

    def __str__(self):
        return f"{self.name} ({self.get_room_type_display()})"

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Кімната")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    start_date = models.DateField(verbose_name="Дата початку")
    end_date = models.DateField(verbose_name="Дата завершення")
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Перевірка логіки дат (ТЗ пункт 1.1)
        if self.start_date and self.end_date:
            if self.start_date >= self.end_date:
                raise ValidationError("Дата початку має бути раніше дати завершення.")
    
    def __str__(self):
        return f"Бронювання {self.room.name} користувачем {self.user.username}"