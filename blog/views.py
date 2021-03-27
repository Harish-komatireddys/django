from django.shortcuts import render
from blog.models import Category, Post, Comment
from .forms import CommentForm

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts
    }

    return render(request, 'index.html', context)


def details(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                body=form.cleaned_data['body'],
                author=form.cleaned_data['author'],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)

    context = {
        'post': post,
        'comments': comments,
        'form': form
    }

    return render(request, 'details.html', context)


def blog_category(request, category):
    posts = Post.objects.filter(
        category__name__contains=category
    ).order_by(
        '-created_on'
    )

    context = {
        'posts': posts,
        'category': category
    }

    return render(request, 'category.html', context)