from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    
    context = {
        'posts':posts
    }
    return render(request, 'home.html', context)

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    context = {
        'post':post
    }
    return render(request, 'detail.html', context)

def create_post(request):
    form = PostForm()
    
    if(request.method == 'POST'):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('home')
    context = {
        'form':form
    }
    return render(request, 'create.html', context)

def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES, instance = post)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form':form,
        'post':post
    }
    return render(request, 'update.html', context)

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if(request.method == 'POST'):
        post.delete()
        return redirect('home')
    context = {
        'post':post
    }
    return render(request, 'delete.html', context)