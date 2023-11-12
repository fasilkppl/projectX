"""projectx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.index_func, name='home_pg'),
    path('home/', user_views.index_func, name='home_pg'),
    path('register/', user_views.register_func, name='register_pg'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login_pg'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout_pg'),
    path('details/<int:pk>/', user_views.details, name='details_pg'),
    path('payment/', user_views.payment, name='payment_pg'),




]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

