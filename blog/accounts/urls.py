from django.urls import path, include
from . import views

app_name = "users"

urlpatterns = [
    path('auth/', views.auth, name = "auth"),
    path('logout/', views.user_logout, name = "logout"),
    path('register/', views.user_register, name = "register"),
    path('login/', views.auth, name = "auth"),

]
