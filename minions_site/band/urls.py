from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shows/', views.ShowList.as_view(), name='shows'),
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),
]
