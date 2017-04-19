from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Comment
from datetime import datetime
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ArticleForm, CommentForm
from django.shortcuts import redirect, get_object_or_404

# Create your views here.

def home(request):
    posts = Article.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list' : post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
        comment_list = Comment.objects.filter(article=post)
    except Article.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = post
            comment.user_name = request.user
            comment.save()
            return redirect('/article/' + str(id))
    else:
        form = CommentForm()
    return render(request, 'post.html', {'post' : post, 'comment_list' : comment_list, 'form' : form})

def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})

def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list, 'error' : False})

def about_us(request):
    return render(request, 'aboutus.html')

def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact = tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})

def create_notice(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.author = request.user
            notice.save()
            return redirect('/article')
    else:
        form = ArticleForm()
    return render(request, 'new_notice.html', {'form' : form})

def post_comment(request, article_id):#unavaliable
    if request.method.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_name = request.user
            comment.save()
            return redirect('/article')
    else:
        form = CommentForm()
        return render(request, 'post.html', {'form' : form})

def edit_post(request, id):
    post = get_object_or_404(Article, pk=id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/article/' + id, pk=post.pk)
    else:
        form = ArticleForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def del_post(request, id):
    post = get_object_or_404(Article, pk=id)
    post.delete()
    return redirect('/article')