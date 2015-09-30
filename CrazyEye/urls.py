"""CrazyEye URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from web import views,api_urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.dashboard ),
    url(r'^hosts/$',views.hosts, name='host_list' ),
    url(r'^hosts/multi/$',views.hosts_multi),
    url(r'^hosts/crontab/$',views.crontab),
    url(r'^multi_task/log/deatail/(\d+)/$',views.multi_task_log_detail,name='multi_task_log_detail'),
    url(r'^hosts/multi/filetrans$',views.hosts_multi_filetrans),
    url(r'^api/',include(api_urls)),
    url(r'^personal/',views.personal,name='personal'),
    url(r'^user_audit/(\d+)/$',views.user_audit, name='user_audit'),
    url(r'^logout/',views.logout,name='logout'),




    url(r'^login/$',views.login,name='login'),

    #url(r'^account/login/$',views.account_auth),
    url(r'^accounts/profile/$',views.personal),

    #test below
    url(r'^register/$', views.register),
    url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.article_detail,{'test':'haa'})
]