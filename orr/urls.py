from django.urls import path
from . import views

urlpatterns = [
    path("", views.resources, name="resources"),
    path("article/", views.display_article, name="display article")
]
