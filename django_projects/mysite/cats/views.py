from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cats.models import Cat, Breed

class CatList(LoginRequiredMixin, View):
    def get(self, request):
        bc = Breed.objects.count()
        cl = Cat.objects.all()

        ctx = {'breed_count': bc, 'cat_list': cl}
        return render(request, 'cats/cat_list.html', ctx)

class BreedList(LoginRequiredMixin, View):
    def get(self, request):
        bl = Breed.objects.all()
        ctx = {'breed_list': bl}
        return render(request, 'cats/breed_list.html', ctx)
    
# Cat views
class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')
    template_name = 'cats/cat_form.html'  # Used for creating cats

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')
    template_name = 'cats/cat_form.html'  # Used for updating cats

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')
    template_name = 'cats/cat_confirm_delete.html'  # Used for deleting cats

# Breed views
class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')
    template_name = 'cats/breed_form.html'  # Used for creating breeds

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')
    template_name = 'cats/breed_form.html'  # Used for updating breeds

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')
    template_name = 'cats/breed_confirm_delete.html'  # Used for deleting breeds