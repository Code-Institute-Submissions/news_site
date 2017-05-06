from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ArticlePostForm
from django.utils import timezone
from .models import Article
from django.shortcuts import redirect

# Create your views here.
def get_index(request):
    return render(request, 'index.html')

def article_list(request):
    """
    Create a view that will return a
    list of Posts that were published prior to'now'
    and render them to the 'blogposts.html' template
    """
    articles = Article.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "articles.html", {'articles': articles})


def article_detail(request, id):
    """
    Create a view that return a single
    Post object based on the post ID and
    and render it to the 'postdetail.html'
    template. Or return a 404 error if the
    post is not found
    """
    article = get_object_or_404(Article, pk=id)
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


