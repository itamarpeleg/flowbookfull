from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('one/<str:pk>/', views.one, name="one"),
    path('two/<str:pk>/', views.two, name="two"),
    path('three/<str:pk>/', views.three, name="three"),
]