from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CreateForm
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'title':'Главная страница сайта', 'posts': posts})

def create(request):
    error = ''
    if request.method =='POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = CreateForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request,'create.html', context)

def remark(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'remark.html', {'title':'Редактировать статью', 'posts': posts})

def detail_view(request, id):
    try:
        posts = Post.objects.get(id=id)

        if request.method == "POST":
            posts.title = request.POST.get("title")
            posts.body = request.POST.get("body")
            posts.chek = request.POST.get("chek")
            posts.save()
            return redirect("home")
        else:
            return render(request, "detail.html", {"posts": posts})
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Post not found</h2>")