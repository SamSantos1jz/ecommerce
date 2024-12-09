from django.urls import path
from login import views

urlpatterns = [
    path('register/', views.register_user, name="register" ),
    path('login/', views.login_user, name='login' )
]
