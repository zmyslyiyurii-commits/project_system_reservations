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
from django.contrib.auth import views as auth_views  # Додано для кастомізації входу
from core import views
from core.forms import LoginForm  # Імпортуємо твою форму з підказками

urlpatterns = [
    # Адмінка
    path('admin/', admin.site.urls),
    
    # Кастомний вхід з нашою формою (Логін/Пароль українською)
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='registration/login.html', 
        authentication_form=LoginForm
    ), name='login'),

    # Решта стандартних шляхів (logout тощо)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Реєстрація
    path('signup/', views.signup, name='signup'),
    
    # Головна сторінка та деталі кімнати
    path('', views.room_list, name='room_list'),
    path('room/<int:pk>/', views.room_detail, name='room_detail'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]

# Блок для відображення фото залів
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)