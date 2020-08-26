from django.urls import path
from . import views

urlpatterns = [
    path('index', views.IndexView.as_view(), name='index'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('post/', views.postview, name='post'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('', views.loginview, name='login'),
]
