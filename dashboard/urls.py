from django.urls import path,include
from . import views

urlpatterns = [
    path('dashboard',views.DashBoard,name='dashboard')
    
]
