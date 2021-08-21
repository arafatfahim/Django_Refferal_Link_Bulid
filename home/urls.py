from django.urls import path
from home import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('projects', views.project, name='projects'),
    path('CV', views.cv, name='CV'),
  
]
