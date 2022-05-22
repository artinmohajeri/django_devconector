from django.shortcuts import render

# Create your views here.


def index_function(request):
    return render(request,'blog/index.html',{})

def post_function(request):
    return render(request,'blog/post.html',{})
    
def posts_function(request):
    return render(request,'blog/posts.html',{})