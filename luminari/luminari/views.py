from django.shortcuts import render,get_object_or_404,redirect
from place.models import Place
from django.contrib import messages
from .forms import LoginForm, RegistrationForm,PlaceForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required


def homepage_view(request):
    place = Place.objects.all()
    return render(request,'index.html',{'places':place})


def place_details(request,slug):
    place = get_object_or_404(Place,slug=slug)
    return render(request,'place_details.html',{'place':place})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Login successful.')
                    return redirect('home')
                else:
                    messages.error(request, 'This account is inactive.')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def add_place_view(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Place Added Successfully Thank you")
            return redirect('add_place')
        else:
            messages.error(request,"Failed to add Place please correct the error")
    else:
        form = PlaceForm()
    return render(request,'add_place.html',{'form':form})

def about_us(request):
    return render(request,'about_us.html',{})


def search_place(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Place.objects.filter(place_title__icontains=query)
    context = {
        'query':query,
        'results':results
    }
    return render(request,'search_results.html',context)

def index(request):
    query = request.GET.get('q','')
    if query:
        places = Place.objects.filter(place_title__icontains=query)
    else:
        places = Place.objects.all()
    
    context = {
        'palces':places,
        'query':query
    }
    return render(request,'index.html',context)

def profile_views(request):
    user = request.user
    context = {
        'username':user.username,
        'email':user.email
    }
    return render(request,'profile.html',context)
    
def about_shi(request):
    return render(request,'shiva.html')

def about_sin(request):
    return render(request,'sindhuja.html')

def about_sam(request):
    return render(request,'sambrama.html')

def intern_view(request):
    return render(request,'intern.html')