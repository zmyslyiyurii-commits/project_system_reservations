from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

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
        # 1. Перевірка, щоб дата початку була раніше дати завершення
        if self.start_date and self.end_date:
            if self.start_date >= self.end_date:
                raise ValidationError("Дата початку має бути раніше дати завершення.")
            
            # 2. Перевірка, щоб не бронювали на минуле
            if self.start_date < timezone.now().date():
                raise ValidationError("Не можна забронювати кімнату на минулу дату.")

            # 3. ПЕРЕВІРКА НА ПЕРЕТИН ДАТ (Пункт 1.2 ТЗ)
            # Шукаємо бронювання цієї ж кімнати, де дати перетинаються з нашими
            overlapping_bookings = Booking.objects.filter(
                room=self.room,
                start_date__lt=self.end_date,
                end_date__gt=self.start_date
            ).exclude(pk=self.pk) # Не рахуємо поточне бронювання при редагуванні

            if overlapping_bookings.exists():
                raise ValidationError(f"Кімната '{self.room.name}' уже зайнята на цей період.")

    def save(self, *args, **kwargs):
        self.full_clean() # Викликаємо clean() перед збереженням у базу
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Бронювання {self.room.name} ({self.start_date} - {self.end_date})"
    
# python manage.py runserver