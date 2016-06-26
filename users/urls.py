"""users URL Configuration

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
from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^miembros/$', views.index, name='members'),
    url(r'^unidades/$', views.units, name='units'),
    url(r'^condecoraciones$', views.awards, name='awards'),

    # ex: /tercio/member/5
    url(r'^member/(?P<member_id>\d+)/$', views.member, name='member'),
    # ex: /tercio/unit/5
    url(r'^unit/(?P<unit_id>\d+)/$', views.unit, name='unit'),
    # ex: /tercio/award/5
    url(r'^award/(?P<award_id>\d+)/$', views.award, name='award'),
]
