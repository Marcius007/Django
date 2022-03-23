from django.urls import path
from .views import profile, register_user, log_in, log_out, ProfileList, ProfileCreateView, ProfileUpdateView,ProfileDeleteView
from .views import PostList, PostContent,CreatePost,UpdatePost,UserUpdateView


urlpatterns = [
    path('', ProfileList.as_view(), name='home'),
    path('profile/', profile, name='profile'),
    path('register/', register_user, name='register'),
    path('login/', log_in, name='log_in'),
    path('logout/', log_out, name='logout'),
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/<pk>', ProfileUpdateView.as_view(), name="update"),
    path('delete/<pk>', ProfileDeleteView.as_view(), name='delete'),
    path('post/', PostList.as_view(), name='post'),
    path('post_content/<pk>', PostContent.as_view(), name='post_content'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('update_post/<pk>', UpdatePost.as_view(), name='update_post'),
    path('update_profile/<pk>', UserUpdateView.as_view(), name='update_profile')
]
