from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('aboutus/', views.aboutus, name="aboutus"),
]
