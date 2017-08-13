from django.conf.urls import url

from . import views

app_name = 'squrl'
urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^squrl', views.api, name='api'),
    url(r'^db', views.db, name='db'),
    url(r'^(?P<slug>\w{7})$', views.redirect, name='redirect'),
]


