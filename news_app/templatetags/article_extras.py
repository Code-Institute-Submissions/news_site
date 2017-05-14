from django import template
from news_app.models import Article
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('topstories.html')
def top_stories(story):
    stories = Article.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return {'stories': stories}


@register.inclusion_tag('relatedcontent.html')
def related_content(related):
    relatedcontents = Article.objects.filter(category="sport"
        ).order_by('-published_date')
    return {'relatedcontents': relatedcontents}
