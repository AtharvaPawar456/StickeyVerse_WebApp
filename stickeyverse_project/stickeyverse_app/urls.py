# stickeyverse_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all_sticker/', views.all_sticker, name='all_sticker'),
    path('new_arrivals/', views.new_arrivals, name='new_arrivals'),
    path('categories/', views.categories, name='categories'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
