"""Library URL Configuration

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
from app import views as app_views
from character8 import views as character8_views
from character9 import views as character9_views

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^display/$', app_views.display_some, {'template_name' : 'display_some.html'}),
    url(r'^search/$', app_views.search),
    url(r'^contact/$', app_views.contact),
    url(r'^contact/thanks/$', app_views.thanks),

    url(r'^foo/$', character8_views.foo, {"template_name" : "template_1.html"}),
    url(r'^bar/$', character8_views.bar,{"template_name" : "template_2.html"}),

    url(r'^about/$', TemplateView.as_view(template_name="template_1.html")),
]
