from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('breed/<int:breed_id>/', views.BreedDetailView.as_view(), name='breed_detail'),
    path('breed/create/', views.BreedCreateView.as_view(), name='breed_create'),
    path('breed/<int:breed_id>/update/', views.BreedUpdateView.as_view(), name='breed_update'),
    path('dog/<int:dog_id>/', views.DogDetailView.as_view(), name='dog_detail'),
    path('dog/<int:dog_id>/update/', views.DogUpdateView.as_view(), name='dog_update'),
    path('breeds/', views.BreedListView.as_view(), name='breed_list'),
    path('dog/create/<int:breed_id>/', views.DogCreateView.as_view(), name='dog_create'),
]