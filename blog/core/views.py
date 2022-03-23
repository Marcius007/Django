from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import PostUpdateForm, RegisterForm, CreateProfileForm, CreatPost, UserUpdateForm
from .models import Profile, Post, UserRole, User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ProfileList(LoginRequiredMixin, ListView):
    model = Profile
    paginate_by = 2
    login_url = 'login/'
    template_name = 'profile_tab.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['profiles'] = Profile.objects.get(id=1)
    #     return context sitas ziuri contexta


class ProfileCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'profile.create_profile'
    model = Profile
    form_class = CreateProfileForm
    template_name = 'create.html'
    success_url = '/profile'


class ProfileUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'profile.change_profile'
    model = Profile
    fields = '__all__'
    template_name = 'update.html'
    success_url = '/profile'


class ProfileDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'profile.delete_profile'
    model = Profile
    template_name = 'delete_user.html'
    success_url = '/profile'


class PostList(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'posts'
    # extra_context = {'new':Post.objects.filter(pub_date__endswith=datetime.date(datetime.today()))}
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['profiles'] = Profile.objects.get(id=1)
    #     return context


class PostContent(PermissionRequiredMixin, DetailView):
    permission_required = 'post.view_post'
    model = Post
    template_name = 'post_content.html'
    # extra_context = {'content':Post.objects.filter()}
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['object'] = Post.objects.all()
    #     return context


class CreatePost(PermissionRequiredMixin, CreateView):
    permission_required = 'post.change_post'
    model = Post
    form_class = CreatPost
    template_name = 'create_post.html'
    success_url = '/post'


class UpdatePost(PermissionRequiredMixin, UpdateView):
    permission_required = 'post.change_post'
    model = Post
    form_class = PostUpdateForm
    template_name = 'update_post.html'
    success_url = '/post'

    # def get_form(self):
    #     form = super().get_form()
    #     form.fields['pub_date'].widget = DateTimePickerInput()
    #     return form


@login_required(login_url='log_in')
def profile(request):
    # user_rol = User.objects.filter(to_be_listed=True)
    # context = {
    #     'user_role': user_rol.get_user_role_id_id_dispay()
    # }
    return render(request, 'profile_data.html')


def register_user(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Your acc was created')
            return redirect('log_in')
        else:
            messages.add_message(request, messages.ERROR, 'Fail to create Acc')
            return redirect('register')
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


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'profile_update.html'
    success_url = '/profile'



