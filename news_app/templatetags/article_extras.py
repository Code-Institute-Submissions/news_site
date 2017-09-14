from django import template
from news_app.models import Article
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('topstories.html', takes_context=True)
def top_stories(context, story):
    article = context['article']
    stories = Article.objects.filter(published_date__lte=timezone.now()
         ).exclude(pk=article.pk).order_by('-published_date')
    return {'stories': stories}


@register.inclusion_tag('relatedcontent.html', takes_context=True)
def related_content(context):
    article = context['article']
    relatedcontents = Article.objects.filter(category=article.category
        ).exclude(pk=article.pk).order_by('-published_date')
    return {'relatedcontents': relatedcontents}
