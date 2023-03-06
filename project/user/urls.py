from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('signup/', signup_function, name="signup"),
    path('signin/', signin_function, name="signin"),
    path('signout/', signout_function, name="signout"),
]
