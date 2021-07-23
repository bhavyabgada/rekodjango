app_name = "posts"

from django.urls import path

from .views import CreatePostView, Reko

urlpatterns = [
    path('reko/', Reko, name='reko'),
    path('', CreatePostView.as_view(), name='add_post')
]