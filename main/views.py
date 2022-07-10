from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from main.forms import CreateNewPost, UpdatePost, CommentSection
from main.models import Blog, Comment

# Create your views here.
def base(response):
    return render(response, 'main/base.html')

class index(ListView):
    model = Blog
    template_name = 'main/index.html'
    ordering = ['-created_at']

class create(CreateView):
    model = Blog
    template_name = 'main/create.html'
    form_class = CreateNewPost

class update(UpdateView):
    model = Blog
    template_name = 'main/update.html'
    form_class = UpdatePost

class delete(DeleteView):
    model = Blog
    template_name = 'main/delete.html'
    success_url = reverse_lazy('index')

def blogpost(response, pk):
    blog = Blog.objects.get(id=pk)
    if response.method == "POST":
        form = CommentSection(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            c = form.cleaned_data["comment"]
            blog.comments.create(name=n, comment=c)
            return HttpResponseRedirect("/%i" %blog.id)
        else:
            print("invalid code")

    else:
        form = CommentSection()
        return render(response, 'main/post.html', {'blog':blog, 'form':form})

def public_profile(response, id):
    post = Blog.objects.filter(author = id)
    return render(response, 'main/public_profile.html', {'post':post})

def search(response):
    return render(response, 'main/search.html')