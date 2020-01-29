from django.urls import path
from django.contrib import admin

from loanapp import views as loan_views

urlpatterns = [
 path('response/', loan_views.responseform),
 path('thankyou/', loan_views.responseform),
 
]