from turtle import title
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from main.forms import CreateNewPost, UpdatePost, CommentSection
from main.models import Blog, Comment
from django.contrib.auth.models import auth, User


# Create your views here.
def base(response):
    return render(response, 'main/base.html')

class index(ListView):
    model = Blog
    template_name = 'main/index.html'
    ordering = ['-created_at']
    paginate_by = 10

class UserPost(ListView):
    model = Blog
    template_name = 'main/user_posts.html'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Blog.objects.filter(author=user.id).order_by('-created_at')

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
