from django.shortcuts import render, get_object_or_404
from .models import Breed, Dog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

def home(request):
    breeds = Breed.objects.all()
    return render(request, 'home.html', {'breeds': breeds})
class BreedDetailView(DetailView):
    model = Breed
    template_name = 'breed_detail.html'
    context_object_name = 'breed'

class BreedListView(ListView):
    model = Breed
    template_name = 'breed_list.html'
    context_object_name = 'breeds'


def dog_detail(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id)
    return render(request, 'dog_detail.html', {'dog': dog})
