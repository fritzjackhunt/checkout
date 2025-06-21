from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('checkoutpage', views.form_view, name='checkoutpage'),
    path('success', views.success_view, name='success'),
]