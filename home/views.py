from django.shortcuts import render
from articles.models import Post

# Create your views here.

def index(request):
    """
    A view to return the index page with article listings
    """

    latest_posts = Post.objects.filter(status=1).order_by('-created_on')[:4]
    context = {
        'latest_posts': latest_posts,
    }

    return render(request, 'home/index.html', context)
