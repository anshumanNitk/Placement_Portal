from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.DashBoard,name='dashboard'),
    path('job',views.JobSec,name='job'),
    path('manage',views.Manage,name='Manage')
    
    
]

    
     