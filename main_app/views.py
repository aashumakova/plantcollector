from django.shortcuts import render, redirect
from .models import Plant 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import WateringForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', { 'plants': plants
    })

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    watering_form = WateringForm()
    return render(request, 'plants/detail.html', { 'plant': plant, 'watering_form': watering_form
    })

class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'

class PlantUpdate(UpdateView):
    model = Plant
    fields = ['species', 'light', 'age']

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants'

def add_watering(request, plant_id):
    #create ModelForm instance using the data that was submitted in the form
    form = WateringForm(request.POST)
    #validate the form
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect('detail', plant_id=plant_id)
