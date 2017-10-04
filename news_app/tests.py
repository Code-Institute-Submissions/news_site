from django.test import TestCase
from .views import home, sport_landing, article_list, article_detail
from django.core.urlresolvers import resolve
from .models import Article
from django.shortcuts import render_to_response

class UrlTests(TestCase):
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, home)

    def test_sport_resolves(self):
        sport_page = resolve('/sport/')
        self.assertEqual(sport_page.func, sport_landing)

    def test_article_list_resolves(self):
        article_list_page = resolve('/articles/')
        self.assertEqual(article_list_page.func, article_list)

    def test_article_detail_resolves(self):
        article_detail_page = resolve('/articles/12/')
        self.assertEqual(article_detail_page.func, article_detail)


class ViewTests(TestCase):
    fixtures = ['news_app']


    def test_home_content_is_correct(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "home.html")
        home_page_template_output = render_to_response("home.html").content
        self.assertEqual(home_page.content, home_page_template_output)

    '''def test_sport_content_is_correct(self):
        sport_page = self.client.get('/sport/')
        self.assertTemplateUsed(sport_page, "categorylanding.html")
        sport_page_template_output = render_to_response("categorylanding.html",
                                                          {'article':
                Article.objects.all()}).content
        self.assertEqual(sport_page.content, sport_page_template_output)'''

    def test_article_content_is_correct(self):
        article_page = self.client.get('/articles/28/')
        self.assertTemplateUsed(article_page, "article.html")
        article_page_template_output = render_to_response("article.html",
                                                          {'article':
                Article.objects.all()}).content
        self.assertEqual(article_page.content, article_page_template_output)


