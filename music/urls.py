from django.conf.urls import patterns, include, url

urlpatterns = patterns('music.views',
    url(r'^$', 'home', name='home'),
)