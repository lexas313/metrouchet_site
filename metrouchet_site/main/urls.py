from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<slug:slug>', views.Index.as_view(), name='index'),
    path('poverka_schetchikov_vody/', views.PoverkaVody.as_view(), name='poverka_schetchikov_vody'),
    path('poverka_schetchikov_vody/<slug:slug>/', views.PoverkaVody.as_view(), name='poverka_schetchikov_vody'),
    path('zamena_schetchikov_vody/', views.ZamenaVody.as_view(), name='zamena_schetchikov_vody'),
    path('zamena_schetchikov_vody/<slug:slug>/', views.ZamenaVody.as_view(), name='zamena_schetchikov_vody'),
    path('ustanovka_schetchikov_vody/', views.UstanovkaVody.as_view(), name='ustanovka_schetchikov_vody'),
    path('ustanovka_schetchikov_vody/<slug:slug>/', views.UstanovkaVody.as_view(), name='ustanovka_schetchikov_vody'),

    path('privacy_policy/', TemplateView.as_view(template_name='main/privacy_policy.html'), name='privacy_policy'),
    path('order_service/', views.OrderServiceFormView.as_view(), name='order_service'),
    path('call_back/', views.CallBackFormView.as_view(), name='call_back'),
]