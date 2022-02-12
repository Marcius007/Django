from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm, CreateProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView, CreateView, UpdateView


class ProfileList(ListView):
    model = Profile
    template_name = 'profile_tab.html'


class ProfileCreateView(CreateView):

    model = Profile
    form_class = CreateProfileForm
    template_name = 'create.html'
    success_url = '/profile'


class ProfileUpdateView(UpdateView):
    model = Profile
    fields = '__all__'
    template_name = 'update.html'
    success_url = '/profile'


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'delete_user.html'
    success_url = '/profile'


@login_required(login_url='log_in')
def home(request):
    return render(request, 'index.html')


@login_required(login_url='log_in')
def profile(request):
    users = Profile.objects.all()
    context = {
        'obj': users,
    }

    return render(request, 'profile_tab.html', context)


def register_user(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('log_in')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('log_in')


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account is not active!")
        else:
            return HttpResponse("Please try again!")
    return render(request, 'log_in.html', {})
