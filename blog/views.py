from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
<<<<<<< HEAD
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts' : posts})
=======
        return render(request, 'blog/post_list.html', {})
>>>>>>> 9de22a31551c63c4f8215ee6144bf326d38ba5c7
