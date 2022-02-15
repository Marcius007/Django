from django.urls import path
from .views import profile, register_user, log_in, log_out, ProfileList, ProfileCreateView, ProfileUpdateView,ProfileDeleteView
from .views import PostList


urlpatterns = [
    path('', ProfileList.as_view(), name='home'),
    path('profile/', profile, name='profile'),
    path('register/', register_user, name='register'),
    path('login/', log_in, name='log_in'),
    path('logout/', log_out, name='logout'),
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/<pk>', ProfileUpdateView.as_view(), name="update"),
    path('delete/<pk>', ProfileDeleteView.as_view(), name='delete'),
    path('post/', PostList.as_view(), name='post')
]
