from django.urls import path

from .views import registration, profile_form, userprofile, login_form, logout_form

app_name = 'user'

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', login_form, name='login'),
    path('logout', logout_form, name='logout'),
    path('profile', userprofile, name='profile'),
    path('profile_update/', profile_form, name='profile_update')
]