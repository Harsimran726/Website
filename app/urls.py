
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('home',views.home, name='home'),
    path('product',views.product, name='product'),
    path('contact',views.contact, name='contact'),
    path('service',views.services, name='services'),
    path('blog',views.blog, name='blog'),
    path("ask_question/",views.ask_question, name='ask_question'),
    path('chat/',views.chat, name='chatbot'),
    path('ai-chatbot',views.chatbot, name='chatbot'),
    path('<str:slug>/', views.post, name='post_detail'),	
    path('user_detail',views.user_detail,name='user_detail'),
    path('sitemap',views.sitemap,name='sitemap'),	 
    path('robots.txt',views.robots,name='Robots.txt'),	
    path('Ads',views.Ads,name='Ads'),	
    path('sw.js',views.sw,name='adsyffl'),

    
]