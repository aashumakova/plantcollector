from django.shortcuts import render

plants = [
    {'name': 'Morgan', 'kingdom': 'Plantae', 'species': 'Monstera xanthospatha', 'performance': 'bright to medium-bright indirect light','age': 1},
    {'name': 'Audrey', 'kingdom': 'Plantae', 'species': 'Ficus benghalensis', 'performance': 'bright indirect light','age': 1},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    return render(request, 'plants/index.html', { 'plants': plants
    })
