from django import template
from news_app.models import Article
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('mainnews.html')
def main_stories(story):
    stories = Article.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return {'stories': stories}


@register.inclusion_tag('sportheadlines.html')
def sport_headlines(story):
    sportheadlines = Article.objects.filter(category="sport"
        ).order_by('-published_date')
    return {'sportheadlines': sportheadlines}

@register.inclusion_tag('polheadlines.html')
def politics_headlines(story):
    polheadlines = Article.objects.filter(category="politics"
        ).order_by('-published_date')
    return {'polheadlines': polheadlines}

@register.inclusion_tag('funheadlines.html')
def funny_headlines(story):
    funheadlines = Article.objects.filter(category="fun"
        ).order_by('-published_date')
    return {'funheadlines': funheadlines}


@register.inclusion_tag('morenews.html')
def more_news():
    morenews = Article.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return {'morenews': morenews}

@register.inclusion_tag('moresport.html')
def more_sport():
    moresport = Article.objects.filter(category="sport"
        ).order_by('-published_date')
    return {'moresport': moresport}

@register.inclusion_tag('morepol.html')
def more_pol():
    morepol = Article.objects.filter(category="politics"
        ).order_by('-published_date')
    return {'morepol': morepol}

@register.inclusion_tag('morefun.html')
def more_fun():
    morefun = Article.objects.filter(category="fun"
        ).order_by('-published_date')
    return {'morefun': morefun}
