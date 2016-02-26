"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
# from django.con.urls.defaults import *
from mysite.views import hello, my_homepage_view, display_meta
from django.contrib import admin
from mysite.books import views
admin.autodiscover()

urlpatterns = [
    url('^hello/$', hello),
    url('^$', my_homepage_view),
    url(r'^admin/', include(admin.site.urls)),
    url('^displaymeta/$', display_meta),
    url(r'^search-form/$', views.search_form),
#    url(r'^search/$', views.search),
]
