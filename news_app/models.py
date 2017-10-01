from django.db import models, transaction
from django.utils import timezone
from model_utils.fields import MonitorField, StatusField
from model_utils import Choices
from tinymce import models as tinymce_models
from django.conf import settings


class Article(models.Model):
    author = models.ForeignKey('accounts.User')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    intro = models.CharField(max_length=1000)
    content = tinymce_models.HTMLField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = MonitorField(monitor='status', when=['published'])
    STATUS = Choices(('draft', 'Draft'), ('published', 'Published'))
    status = StatusField()
    is_the_chosen_one = models.BooleanField(default=False)
    twitterStatus = models.CharField(max_length=100)
    youtubeVideo = models.CharField(max_length=100)
    instaPic = models.CharField(max_length=200)
    category = models.CharField(max_length=256, choices=[
        ('sport', 'Sport'),
        ('politics', 'Politics'),
        ('news', 'News'),
        ('fun', 'Fun'),
        ('music', 'Music'),
    ], default='news')

    @transaction.atomic
    def save(self, *args, **kwargs):
        if self.is_the_chosen_one:
            Article.objects.filter(
                is_the_chosen_one=True).update(is_the_chosen_one=False)
        super(Article, self).save(*args, **kwargs)



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title