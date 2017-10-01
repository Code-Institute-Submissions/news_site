from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ArticlePostForm
from django.utils import timezone
from .models import Article
from django.shortcuts import redirect
from accounts.views import login

def get_index(request):
    return render(request, 'index.html')

# List of all articles, draft or published
@login_required(login_url='/login/')
def article_list(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "articles.html", {'articles': articles})


def article_detail(request, id):
    article = get_object_or_404(Article, pk=id)
    if request.user.is_anonymous and article.status == 'draft':
        return redirect(login)
    else:
        return render(request, "article.html", {'article': article})

@login_required(login_url='/login/')
def new_article(request):
    if request.method == "POST":
        form = ArticlePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(article_detail, post.pk)
    else:
        form = ArticlePostForm()
    return render(request, 'articlepostform.html', {'form': form})

@login_required(login_url='/login/')
def edit_article(request, id):
    article = get_object_or_404(Article, pk=id)
    if request.method == "POST":
        form = ArticlePostForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article.author = request.user
            article.published_date = timezone.now()
            article.save()
            return redirect(article_detail, article.pk)

    else:
        form = ArticlePostForm(instance=article)
    return render(request, 'articlepostform.html', {'form': form})

def home(request):
    home = Article.objects.filter(published_date__lte=timezone.now(), status='published'
                                  ).order_by('-published_date')
    return render(request, "home.html", {'home': home})


def sport_landing(request):
    page_title = 'Sport'
    cat_landing = Article.objects.filter(status='published', category='sport', published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "categorylanding.html", {'cat_landing': cat_landing, 'page_title': page_title})

def politics_landing(request):
    page_title = 'Politics'
    cat_landing = Article.objects.filter(status='published', category='politics', published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "categorylanding.html", {'cat_landing': cat_landing, 'page_title': page_title})
