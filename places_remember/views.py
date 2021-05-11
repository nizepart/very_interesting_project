from django.shortcuts import render, redirect
from . models import Memory
from .forms import MemoryForm, CreateUserForm

from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def index(request):
    memories = Memory.objects.order_by('-id')
    return render(request, 'places_remember/index.html', {'memories': memories})


def about(request):
    return render(request, 'places_remember/about.html')


@login_required(login_url='login')
def create(request):
    error = ''
    if request.method == "POST":
        form = MemoryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            error = 'Форма неверная'

    form = MemoryForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'places_remember/create.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        form = CreateUserForm()
        context = {
            'form': form
        }
        return render(request, 'places_remember/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

        return render(request, 'places_remember/login.html')
