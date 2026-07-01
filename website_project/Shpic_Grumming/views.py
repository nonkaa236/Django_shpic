from django.shortcuts import render, get_object_or_404, redirect
from .models import Breed, Dog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy

def home(request):
    breeds = Breed.objects.all()
    return render(request, 'home.html', {'breeds': breeds})

class BreedDetailView(DetailView):
    model = Breed
    template_name = 'breed_detail.html'
    context_object_name = 'breed'
    pk_url_kwarg = 'breed_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dogs'] = Dog.objects.filter(breed=self.object)
        return context

class BreedListView(ListView):
    model = Breed
    template_name = 'breed_list.html'
    context_object_name = 'breeds'


class BreedCreateView(CreateView):
    model = Breed
    template_name = 'breed_create.html'
    context_object_name = 'breed'
    fields = ['name', 'description', 'origin', 'image']
    success_url = reverse_lazy('breed_list')

class BreedUpdateView(UpdateView):
    model = Breed
    template_name = 'breed_update.html'
    context_object_name = 'breed'
    fields = ['name', 'description', 'origin', 'image']
    pk_url_kwarg = 'breed_id'
    
    def get_success_url(self):
        return reverse_lazy('breed_detail', kwargs={'breed_id': self.object.id})

class DogDetailView(DetailView):
    model = Dog
    template_name = 'dog_detail.html'
    context_object_name = 'dog'
    pk_url_kwarg = 'dog_id'

class DogCreateView(CreateView):
    model = Dog
    template_name = 'dog_create.html'
    context_object_name = 'dog'
    fields = ['name', 'breed', 'age', 'description', 'image']
    
    def get_initial(self):
        initial = super().get_initial()
        breed_id = self.kwargs.get('breed_id')
        if breed_id:
            initial['breed'] = Breed.objects.get(pk=breed_id)
        return initial
    
    def get_success_url(self):
        return reverse_lazy('breed_detail', kwargs={'breed_id': self.object.breed.id})

class DogUpdateView(UpdateView):
    model = Dog
    template_name = 'dog_update.html'
    context_object_name = 'dog'
    fields = ['name', 'breed', 'age', 'description', 'image']
    pk_url_kwarg = 'dog_id'
    
    def get_success_url(self):
        return reverse_lazy('dog_detail', kwargs={'dog_id': self.object.id})