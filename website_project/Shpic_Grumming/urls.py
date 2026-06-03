from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('breed/<int:breed_id>/', views.BreedDetailView.as_view(), name='breed_detail'),
    path('dog/<int:dog_id>/', views.dog_detail, name='dog_detail'),
    path('breeds/', views.BreedListView.as_view(), name='breed_list'),
]