from django.urls import path, include
from app.views import *

# app_name = ''

urlpatterns = [
    path('', index, name='index'),
    # path('login', include('authentication.urls'))
    path('about', about, name='about'),
    path('tournament', tournament, name='tournament'),
    path('tournament_detail', tournament_detail, name='tournament_detail'),
    # profile update ...
    path('Profile', PROFILE, name='profile'),
    path('Profile/update', PROFILE_UPDATE, name='profile_update'),
    # login register to path
    path('login/', LOGIN, name='login'),
    path('doLogin/', doLogin, name='doLogin'),
    path('doLogin', doLogout, name='dologout'),

]
