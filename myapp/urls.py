from django.urls import path
from . import views

urlpatterns = [
    path('admins/login/', views.admin_login, name='admin_login'),
    path('admins/home/', views.admin_home, name='admin_home'),
]
