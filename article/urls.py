from django.conf.urls import url
from . import views

app_name = 'article'

urlpatterns = [
    url(r'^$', views.home),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^test/$', views.test),
    url(r'^archives/$', views.archives, name='archives'),
    url(r'^aboutus/$', views.about_us, name='about_us'),
    url(r'^tag(?P<tag>\w+)/$', views.search_tag, name='search_tag'),
    url(r'^create_notice/$', views.create_notice, name='create_notice')
]
