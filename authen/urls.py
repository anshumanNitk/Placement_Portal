from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.UserLogin, name='login'),
    path('signup',views.UserSignUp, name='signup'),
    path('logout',views.logout,name='logout'),
    
    path('dashboard',include('dashboard.urls')),
    path('application',include('application.urls'))
    
]
