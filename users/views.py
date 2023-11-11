from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm
from .models import *


def index_func(request):

    details = Details.objects.all()
    context ={"details" : details}
    return render(request, 'users/index.html',context)


def register_func(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login_pg')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



def details(request, pk):
    detail = get_object_or_404(Details, pk=pk)
    context ={"detail" : detail}
    return render(request,'users/details.html',context)

