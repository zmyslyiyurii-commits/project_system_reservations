from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

class Room(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='rooms', verbose_name="Категорія")
    name = models.CharField(max_length=100, verbose_name="Назва кімнати/місця")
    description = models.TextField(verbose_name="Опис")
    capacity = models.PositiveIntegerField(verbose_name="Місткість (осіб)")
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна за годину")
    image = models.ImageField(upload_to='rooms/', blank=True, null=True, verbose_name="Фото")

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class Meta:
        verbose_name = "Кімната"
        verbose_name_plural = "Кімнати"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Кімната")
    start_time = models.DateTimeField(verbose_name="Початок бронювання")
    end_time = models.DateTimeField(verbose_name="Кінець бронювання")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    def __str__(self):
        return f"{self.user.username} - {self.room.name} ({self.start_time.strftime('%d.%m %H:%M')})"

    class Meta:
        verbose_name = "Бронювання"
        verbose_name_plural = "Бронювання"
        
# python manage.py runserver