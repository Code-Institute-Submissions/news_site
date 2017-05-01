from django.db import models
from django.utils import timezone
from model_utils.fields import StatusField
from model_utils import Choices

class Article(models.Model):
    author = models.ForeignKey('accounts.User')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    intro = models.CharField(max_length=1000)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    STATUS = Choices('draft', 'published')
    status = StatusField()
    twitterStatus = models.CharField(max_length=100)
    youtubeVideo = models.CharField(max_length=100)
    instaPic = models.CharField(max_length=200)



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title