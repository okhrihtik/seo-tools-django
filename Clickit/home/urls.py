import imp
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('pricing', views.pricing, name='pricing'),
    path('tools', views.tools, name='tools'),
    path('tools1', views.tools1, name='tools1'), 
    # path('tools2', views.tools2, name='tools2'), 
    # path('tools3', views.tools3, name='tools3'),

]
