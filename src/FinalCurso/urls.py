from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'apps.core.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': '/'}
    ),
    url(r'^new_product/$', 'apps.stock.views.new_product'),
    url(r'^product_list/$', 'apps.stock.views.product_list'),
)
