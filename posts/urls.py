app_name = "posts"

from django.urls import path

from .views import HomePageView, CreatePostView, Reko # new

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('reko/', Reko, name='reko'),
    path('post/', CreatePostView.as_view(), name='add_post') # new
]