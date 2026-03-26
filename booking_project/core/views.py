from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
            booking.user = request.user  # Прив'язуємо бронювання до того, хто увійшов
            booking.save()
            return redirect('room_list')
    else:
        form = BookingForm()
    
    return render(request, 'core/booking_form.html', {'form': form})