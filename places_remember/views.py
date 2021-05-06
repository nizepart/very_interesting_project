from django.shortcuts import render, redirect
from . models import Memory
from .forms import MemoryForm


# Create your views here.

def index(request):
    memories = Memory.objects.order_by('-id')
    return render(request, 'places_remember/index.html', {'memories': memories})


def about(request):
    return render(request, 'places_remember/about.html')


def create(request):
    error = ''
    if request.method == "POST":
        form = MemoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверная'

    form = MemoryForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'places_remember/create.html', context)
