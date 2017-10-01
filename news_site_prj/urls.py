"""news_site_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from paypal_store import views as paypal_views
from accounts import views as accounts_views
from news_app import views as news_views
from settings.base import MEDIA_ROOT
from paypal.standard.ipn import urls as paypal_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', news_views.home, name='home'),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^article/new/$', news_views.new_article, name='new_article'),
    url(r'^articles/(?P<id>\d+)/$', news_views.article_detail, name="article_detail"),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^articles/(?P<id>\d+)/edit$', news_views.edit_article),
    url(r'^articles/$', news_views.article_list, name='article_list'),
    url(r'^sport/$', news_views.sport_landing, name='sport_landing'),
    url(r'^politics/$', news_views.politics_landing, name='politics_landing'),
    url(r'^tuux4YjAo2U58peXPSC7/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),
    url(r'^products/$', paypal_views.all_products, name='all_products'),


]

if settings.DEBUG:
    import debug_toolbar
urlpatterns += [
    url(r'^__debug__/', include(debug_toolbar.urls)),
]
