from django import forms
from .models import Booking
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# 1. Форма Бронювання (з підтримкою JS розрахунку ціни)
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_time', 'end_time']
        widgets = {
            # Додаємо id: 'id_start_time' та 'id_end_time' для JavaScript
            'start_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local', 
                'class': 'datetime-input', 
                'id': 'id_start_time'
            }),
            'end_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local', 
                'class': 'datetime-input', 
                'id': 'id_end_time'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        
        if start_time and end_time:
            # Перевірка, щоб дата не була в минулому
            if start_time < timezone.now():
                raise forms.ValidationError("❌ Час уже минув.")
            # Перевірка логіки початку/кінця
            if end_time <= start_time:
                raise forms.ValidationError("❌ Кінець має бути пізніше початку.")
        return cleaned_data

# 2. Форма Реєстрації
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Логін', 'class': 'auth-input'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Електронна пошта', 'class': 'auth-input'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Пароль', 'class': 'auth-input'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Повторіть пароль', 'class': 'auth-input'})

# 3. Форма Входу
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Логін', 'class': 'auth-input'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Пароль', 'class': 'auth-input'})