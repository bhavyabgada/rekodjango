from django.shortcuts import render
from django.views.generic import ListView, CreateView  # new
from django.urls import reverse_lazy  # new
import boto3
from djangoProject import settings as s
from .forms import PostForm  # new
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class CreatePostView(CreateView):  # new
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('posts:reko')


def Reko(request):
    latest_questions = Post.objects.last()
    # with open(latest_questions, 'rb') as source_image:
    #     source_bytes = source_image.read()
    client = boto3.client('rekognition', aws_access_key_id=s.AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=s.AWS_SECRET_ACCESS_KEY, region_name=s.AWS_S3_REGION_NAME)
    labels = client.detect_labels(
        Image={'S3Object': {'Bucket': s.AWS_STORAGE_BUCKET_NAME, 'Name': 'images/'+latest_questions.title+'.jpeg'}},
        MinConfidence=95)
    text = client.detect_text(
        Image={'S3Object': {'Bucket': s.AWS_STORAGE_BUCKET_NAME, 'Name': 'images/' + latest_questions.title + '.jpeg'}},
        Filters={
            'WordFilter': {
                'MinConfidence': 95
            },})
    return render(request, 'reko.html', {'request': latest_questions, 'labels': labels, 'text':text})
