from django.urls import path, include
from . import views

app_name = 'user'

urlpatterns = [
    path('ajax_val/', views.ajax_validate_captcha, name='ajax_val'),
    path('refresh_captcha/', views.refresh_captcha, name='refresh_captcha'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]