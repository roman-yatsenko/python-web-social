from django.contrib.auth import views as auth_views
from django.urls import path

from .views import dashboard

urlpatterns = [
    # path('login/', user_login, name='login'),
    
    # url-адреси для входу та виходу
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('', dashboard, name='dashboard')
]
