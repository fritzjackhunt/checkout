from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('forms', views.form_view, name='forms'),
    path('success', views.success_view, name='success'),
]