from django.urls import path
from . import views

urlpatterns = [
    path('host/<int:host_id>/', views.host_detail, name='host_detail'),
]
