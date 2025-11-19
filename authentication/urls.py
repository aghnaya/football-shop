from django.urls import path
from .views import register_api, login_api, logout_api

app_name = 'authentication'

urlpatterns = [
    path('register/', register_api, name='register_api'),
    path('login/', login_api, name='login_api'),
    path('logout/', logout_api, name='logout_api'),
]
