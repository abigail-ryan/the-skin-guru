from . import views
from django.urls import path

urlpatterns = [
    path('', views.contact_us, name='contact'),
]