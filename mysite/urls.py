from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import squrl.views

# Examples:
# url(r'^$', 'mysite.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', squrl.views.index, name='index'),
    url(r'^db', squrl.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
