from .models import Memory
from django.forms import ModelForm, TextInput, Textarea


class MemoryForm(ModelForm):
    class Meta:
        model = Memory
        fields = ['title', 'task']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
        }