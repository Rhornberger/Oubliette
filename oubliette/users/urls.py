from django.urls import path
from .views import register, profile, home, about
from users import views as user_views


app_name = 'users'
urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('', home, name='home'),
    path('about/', about, name='about')
]
