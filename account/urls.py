from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup,name='sign'),
    path('login/', views.login,name='log'),
    path('logout/', views.logout,name='logout'),
]
