from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Room, Booking
# Використовуємо твої кастомні форми
from .forms import BookingForm, SignUpForm, LoginForm

# 1. Список всіх кімнат (Головна сторінка)
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'core/room_list.html', {'rooms': rooms})

# 2. Деталі кімнати та форма бронювання
def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    form = BookingForm()
    error_message = None

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
            
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.user = request.user
            
            # Перевірка на накладку часу (Overlap)
            overlap = Booking.objects.filter(
                room=room,
                start_time__lt=booking.end_time,
                end_time__gt=booking.start_time
            ).exists()
            
            if overlap:
                error_message = "❌ Цей зал уже заброньовано на обраний час. Оберіть інший проміжок."
            else:
                booking.save()
                return redirect('my_bookings')

    return render(request, 'core/room_detail.html', {
        'room': room,
        'form': form,
        'error_message': error_message
    })

# 3. Реєстрація користувача
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('room_list')
    else:
        form = SignUpForm() 
    return render(request, 'core/signup.html', {'form': form})

# 4. Особистий кабінет (Мої бронювання)
@login_required
def my_bookings(request):
    # Отримуємо всі бронювання користувача, від нових до старих
    bookings = Booking.objects.filter(user=request.user).order_by('-start_time')
    return render(request, 'core/my_bookings.html', {'bookings': bookings})