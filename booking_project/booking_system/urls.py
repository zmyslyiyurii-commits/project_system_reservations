"""
URL configuration for booking_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    # Адмінка
    path('admin/', admin.site.urls),
    
    # Стандартні шляхи авторизації (login, logout)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Реєстрація
    path('signup/', views.signup, name='signup'),
    
    # Головна сторінка та деталі кімнати
    path('', views.room_list, name='room_list'),
    path('room/<int:pk>/', views.room_detail, name='room_detail'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]

# Це критично важливий блок для відображення завантажених фото
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)