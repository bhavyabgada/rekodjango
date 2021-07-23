from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
import boto3
from djangoProject import settings as s
from .forms import PostForm
from .models import Post


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('posts:reko')


def Reko(request):
    image = Post.objects.last()
    client = boto3.client('rekognition', aws_access_key_id=s.AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=s.AWS_SECRET_ACCESS_KEY, region_name=s.AWS_S3_REGION_NAME)
    labels = client.detect_labels(
        Image={'S3Object': {'Bucket': s.AWS_STORAGE_BUCKET_NAME, 'Name': 'images/' + image.title}},
        MinConfidence=65)
    text = client.detect_text(
        Image={'S3Object': {'Bucket': s.AWS_STORAGE_BUCKET_NAME, 'Name': 'images/' + image.title}},
        Filters={
            'WordFilter': {
                'MinConfidence': 65
            }, })
    return render(request, 'reko.html',
                  {'request': image, 'labels': labels['Labels'], 'text': text['TextDetections']})
