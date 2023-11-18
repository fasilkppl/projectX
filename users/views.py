from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib import messages
from .models import *
from django.http import JsonResponse
from .forms import CustomAuthenticationForm
from django.contrib.auth.decorators import login_required



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
    barber = get_object_or_404(Details, pk=pk)

    slideimages = SlideImage.objects.filter(slideproduct=detail)
    reviews = Review.objects.filter(barber=barber)


    # Fetch the current follower count
    current_follower_count = detail.followers.count()

    context = {
        "detail": detail,
        "slideimages": slideimages,
        "current_follower_count": current_follower_count,
        'barber': barber, 
        'reviews': reviews,
    }

    return render(request, 'users/details.html', context)




def follow_barber(request, pk):
    if request.method == 'POST':
        barber = get_object_or_404(Details, pk=pk)
        

        # Assuming you have a ForeignKey named 'followers' in your Details model
        if request.user in barber.followers.all():
            barber.followers.remove(request.user)
            is_following = False
        else:
            barber.followers.add(request.user)
            is_following = True

        # Update the follower count
        followers_count = barber.followers.count()

        return JsonResponse({
            'success': True,
            'is_following': is_following,
            'followers_count': followers_count,
        })

    return JsonResponse({'success': False, 'error': 'Invalid request'})




@login_required
def add_review(request, pk):
    barber = get_object_or_404(Details, pk=pk)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)  # Include request.FILES to handle uploaded files
        if form.is_valid():
            review = form.save(commit=False)
            review.barber = barber
            review.user = request.user
            review.save()
            return redirect('details', pk=pk)
    else:
        form = ReviewForm()

    return render(request, 'users/add_review.html', {'form': form, 'barber': barber})





def payment(request):
    return render(request,'users/payment.html')






