#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Project URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from wkhtmltopdf.views import PDFTemplateView
from django.views.generic.base import View
from master.views import index, SurveyListView, SurveyCreateView, \
    survey_delete_view, search ,mypdfview, delete , edit, display, inst, RapidSlumAppresalView, insert , upload_pic


from wkhtmltopdf.views import PDFTemplateView
from django.conf import settings
from django.conf.urls.static import static
    



from master.views import ClassBasedView    

admin.autodiscover()

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^master/', include(admin.site.urls)),
    url(r'^surveymapping/', SurveyListView.as_view(),
        name='SurveyCreate'),
    url(r'^surveymapping/(?P<name>\w[a-zA-Z_0-9]+)/$',
        SurveyListView.as_view(), name="SurveyCreate"),
    url(r'AddSurveyMapping/$', SurveyCreateView.as_view(),
        name='survey-add'),
    url(r'^deletesurvey/(?P<survey>[0-9]+)/$', survey_delete_view,
        name='surveydelete'),
    url(r'Survey/(?P<survey>[0-9]+)/$', SurveyCreateView.as_view(),
        name='survey-update'),
 
    url(r'^search/$', search, name="search"),
 
    url(r'^mypdfview/', mypdfview.as_view()), 
 
    url(r'^delete/(?P<Rapid_Slum_Appresal_id>\d+)$', delete, name='delete'),
 
    url(r'^edit/(?P<Rapid_Slum_Appresal_id>\d+)$', edit, name='edit'),
 
    url(r'^display/$', display, name='display'),
 
    url(r'^inst/$', inst, name='inst'),

    
    url(r'^insert/$', insert, name='insert'),

    url(r'^RapidSlumAppresalView/$', RapidSlumAppresalView.as_view(),name='RapidSlumAppresalView'),

    url(r'^cbv/$', ClassBasedView.as_view(), name='cbv'),

    url(r'^cbv/(?P<Rapid_Slum_Appresal_id>\d+)$', ClassBasedView.as_view(), name='cbv'),
  
    url(r'^upload_pic/$',upload_pic, name='upload_pic'),
    
]
 


            