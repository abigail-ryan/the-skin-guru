from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delivery/', views.delivery_info, name='delivery'),
]
