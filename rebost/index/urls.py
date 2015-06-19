from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

urlpatterns = patterns(
    'rebost.index.views',

    url(r'^/?$', 'index', name='index'),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
)
