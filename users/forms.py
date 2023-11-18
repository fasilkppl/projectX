from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, get_user_model
from .models import *





class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username or Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    class Meta:
        fields = ['username', 'password']

    def clean(self):
        username_or_email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username_or_email and password:
            # Check if the input is a valid email address
            if '@' in username_or_email:
                # Try to authenticate using email
                self.user_cache = self.authenticate_by_email(username_or_email, password)
            else:
                # Try to authenticate using the default username
                self.user_cache = authenticate(request=self.request, username=username_or_email, password=password)

            if self.user_cache is None:
                raise self.get_invalid_login_error()

        return self.cleaned_data

    def authenticate_by_email(self, username_or_email, password):
        """
        Authenticate using the provided email and password.
        """
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username_or_email)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None
    




class ReviewForm(forms.ModelForm):
    RATING_CHOICES = (
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    )

    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)
    review_user_image = forms.ImageField(required=False)  # Include the image upload field
    
    class Meta:
        model = Review
        fields = ['comment', 'rating', 'review_user_image']  # Add 'review_user_image' field
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 5}),
        }
