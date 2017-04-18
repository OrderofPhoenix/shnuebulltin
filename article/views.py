from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from datetime import datetime
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ArticleForm
from django.shortcuts import redirect

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
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})

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
    return render(request, 'editor.html', {'form' : form})
