# crop_prices_app/urls.py
from django.urls import path
from .views import login_view, logout_view, prices, home

app_name = 'crop_prices'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('prices/', prices, name='prices'),
    path('home/', home, name='home'),
]
