from django.conf.urls import include, url
from django.contrib import admin


from .views import querydashboard, surveyformlist, questionlist

urlpatterns = [
    url(r'^$', querydashboard, name='querydashboard'),
    url(r'^surveyformlist/$', surveyformlist, name='surveyformlist'),
    url(r'^questionlist/$', questionlist, name='questionlist'),
]