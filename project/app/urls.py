from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('home',views.home, name='home'),
    path('product',views.product, name='product'),
    path('contact',views.contact, name='contact'),
    path('service',views.services, name='services'),
    path('blog',views.blog, name='blog'),
    path('ai-chatbot',views.chatbot, name='chatbot'),
    path('<str:slug>/', views.post, name='post_detail'),
    
]