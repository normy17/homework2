from django.urls import path

from web.views import *

urlpatterns = [
    path("", main_view, name="main"),
    path("registration/", registration_view, name="registration"),
    path("auth/", auth_view, name="auth"),
    path("logout/", logout_view, name="logout"),
    path("numbers/", numbers, name="numbers"),
    path("reg/", reg_view, name='reg'),
    path("progday/", programmer_day, name='prog_day')
]