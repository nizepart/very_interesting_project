from .models import Memory
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MemoryForm(ModelForm):
    class Meta:
        model = Memory
        fields = ['title', 'task', 'location']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите комментарий'
            })
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта'
            }),
        }