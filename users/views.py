from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, CustomAuthenticationForm
from django.contrib import messages
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







from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to a success page.
            return redirect('home_pg')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'users/login.html', {'form': form})




def details(request, pk):
    detail = get_object_or_404(Details, pk=pk)
    context ={"detail" : detail}
    return render(request,'users/details.html',context)





def payment(request):
    return render(request,'users/payment.html')



