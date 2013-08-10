from django.conf.urls import patterns, include, url

urlpatterns = patterns('polls.views',
    # Examples:
    url(r'^$', 'index'),
    url(r'^(?P<poll_id>\d+)/$', 'detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    )