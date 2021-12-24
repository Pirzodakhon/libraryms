from django.urls import path

from projects.views import main
from . import views

urlpatterns = [
    path('', views.main, name="projects"),
    path('update-book/<str:pk>/', views.updateBook, name = "update_book"),
    path('add_book/', views.add_books, name="add_book"),
]