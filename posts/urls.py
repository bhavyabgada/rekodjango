app_name = "posts"

from django.urls import path

from .views import HomePageView, CreatePostView, Reko # new

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('', Reko, name='reko'),
    path('post/', CreatePostView.as_view(), name='add_post') # new
]