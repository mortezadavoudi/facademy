from django.urls import path
from .views import *

app_name = "client"

urlpatterns = [
    path('', dashboard, name='index'),
    path('sms/', sendsms, name='sms'),
    # path('signing/', signing, name='login'),
    # path('logout', logout, name='logout'),
]