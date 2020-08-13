from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name='portfolio-home '),
    path('aboutme/', views.aboutme, name='portfolio-aboutme')
]