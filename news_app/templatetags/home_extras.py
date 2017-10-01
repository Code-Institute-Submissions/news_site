from django import template
from news_app.models import Article
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('hero.html')
def hero(story):
    hero = Article.objects.filter(status='published', is_the_chosen_one=True)
    return {'hero': hero}

@register.inclusion_tag('mainnews.html')
def main_stories(story):
    stories = Article.objects.filter(status='published',  published_date__lte=timezone.now()
        ).exclude(category="sport").exclude(is_the_chosen_one=True).order_by('-published_date')
    return {'stories': stories}


@register.inclusion_tag('mainnews.html')
def sport_headlines(story):
    stories = Article.objects.filter(status='published', category="sport"
        ).exclude(is_the_chosen_one=True).order_by('-published_date')
    return {'stories': stories}

@register.inclusion_tag('polheadlines.html')
def politics_headlines(story):
    polheadlines = Article.objects.filter(status='published', category="politics"
        ).order_by('-published_date')
    return {'polheadlines': polheadlines}

@register.inclusion_tag('polheadlines.html')
def funny_headlines(story):
    polheadlines = Article.objects.filter(status='published', category="fun"
        ).order_by('-published_date')
    return {'polheadlines': polheadlines}


@register.inclusion_tag('morenews.html')
def more_news():
    section_title = 'News'
    morenews = Article.objects.filter(status='published',  published_date__lte=timezone.now()
        ).exclude(category="sport").exclude(category="politics").exclude(category="fun").exclude(is_the_chosen_one=True).order_by('-published_date')
    return {'morenews': morenews, 'section_title': section_title}

@register.inclusion_tag('morenews.html')
def more_sport():
    section_title = 'Sport'
    morenews = Article.objects.filter(status='published', category="sport"
        ).exclude(is_the_chosen_one=True).order_by('-published_date')
    return {'morenews': morenews, 'section_title': section_title}

@register.inclusion_tag('morenews.html')
def more_pol():
    section_title = 'Politics'
    morenews = Article.objects.filter(status='published', category="politics"
        ).exclude(is_the_chosen_one=True).order_by('-published_date')
    return {'morenews': morenews, 'section_title': section_title}

@register.inclusion_tag('morenews.html')
def more_fun():
    section_title = 'Fun'
    morenews = Article.objects.filter(status='published', category="fun"
        ).exclude(is_the_chosen_one=True).order_by('-published_date')
    return {'morenews': morenews, 'section_title': section_title}
