from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.service, name = 'service'),
    path('about/', views.about, name = 'about'),
    path('testimonials/', views.testimonials, name = 'testimonials'),
    path('contact/', views.contact, name = 'contact'),
    path('faq/', views.faq, name = 'faq'),
]