from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Room, Booking
from .forms import BookingForm

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'core/room_list.html', {'rooms': rooms})

@login_required
def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()

            # ВІДПРАВКА ПІДТВЕРДЖЕННЯ (Пункт 2.2 ТЗ)
            subject = 'Підтвердження бронювання'
            message = f'Вітаємо, {request.user.username}!\nВаше бронювання кімнати "{booking.room.name}" на період з {booking.start_date} по {booking.end_date} успішно оформлено.'
            from_email = 'admin@bookingsystem.com'
            recipient_list = [request.user.email if request.user.email else 'test@example.com']
            
            send_mail(subject, message, from_email, recipient_list)

            return redirect('room_list')
    else:
        form = BookingForm()
    
    return render(request, 'core/booking_form.html', {'form': form})