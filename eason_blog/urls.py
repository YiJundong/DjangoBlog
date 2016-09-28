#-*-coding:utf-8-*-
"""eason_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from article.views import index, detail, post, test, home, search_tag, blog_search

#不同的django版本，这里的写法不同
#后两个url可以写在article.urls中，然后include过来？
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^index/$', index, name='index'),
    url(r'^tag(?P<tag>\w+)/$', search_tag, name = 'search_tag'),
    url(r'^(?P<id>\d+)/$', detail, name='detail'),
    url(r'^post/(?P<my_args>\d+)/$', post, name='post'),
    url(r'^test/$', test),
    url(r'^search/$', blog_search, name = 'search'),
    ]

