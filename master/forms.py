#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The Django Forms Page for master app"""

import urllib2
import json

from django import forms
from django.conf import settings

from master.models import Survey, City  ,Rapid_Slum_Appresal
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.forms import widgets


SURVEY_LIST = []


class SurveyCreateForm(forms.ModelForm):
    """Create a new survey"""

    kobotool_survey_id = forms.ChoiceField(widget=forms.Select(),
                                           required=True)
    kobotool_survey_url = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        """Initialization"""
        try:
            self.survey = kwargs.pop('survey')
        except KeyError:
            print 'No survey Id'
        super(SurveyCreateForm, self).__init__(*args, **kwargs)
        self.list_i = []
        self.list_i = get_kobo_id_list()
        self.fields['kobotool_survey_id'].choices = self.list_i
        self.fields['kobotool_survey_id'].initial = [0]
        self.fields['kobotool_survey_url'].required = False

        # self.fields['kobotoolSurvey_url'].widget.attrs['readonly'] = True

    class Meta:
        """Metadata for class SurveyCreateForm"""
        model = Survey
        fields = [
            'name',
            'description',
            'city',
            'survey_type',
            'analysis_threshold',
            'kobotool_survey_id',
            ]

    def save(self, *args, **kwargs):
        """Method to create a new Mapping Survey Form"""
        instance = super(SurveyCreateForm, self).save(commit=False)
        try:
            instance.id = self.survey
        except IOError:
            print 'Error for Survey_id'

        kobourl = ''
        data = self.cleaned_data

        for survey_value in SURVEY_LIST:
            if survey_value[0] == data['kobotool_survey_id']:
                kobourl = survey_value[1]

        instance.kobotool_survey_url = kobourl
        instance.save()
        return instance


def get_kobo_id_list():

    # url="http://kc.shelter-associates.org/api/v1/forms?format=json"
    """Method which fetches the KoboCat ID's and URL's from the Kobo Toolbox API"""

    url = settings.KOBOCAT_FORM_URL
    req = urllib2.Request(url)
    req.add_header('Authorization', settings.KOBOCAT_TOKEN)
    resp = urllib2.urlopen(req)
    content = resp.read()
    data = json.loads(content)

    temp_arr = []
    temp_arr.append(('', '-----------'))
    for value in data:
        SURVEY_LIST.append((value['id_string'], value['url']))
        temp_arr.append((value['id_string'], value['id_string']))

    return temp_arr


class LocationWidget(widgets.TextInput):
    """Map Widget"""
    template_name = 'draw.html'
    def render(self, name, value, attrs=None):
        context = {'POLYGON':value}
        return mark_safe(render_to_string(self.template_name, context))


class CityFrom(forms.ModelForm):
    """City Form"""
    shape = forms.CharField(widget=LocationWidget())
    class Meta:
        model = City
        fields = ('name', 'shape', 'state_code', 'district_code', 'city_code')
        exclude = ('created_by', 'created_on')



class Rapid_Slum_AppresalForm(forms.ModelForm):
    approximate_population = forms.IntegerField(required=True)
    toilet_cost = forms.IntegerField(required=True)
    toilet_seat_to_persons_ratio = forms.IntegerField(required=True)
    percentage_with_an_individual_water_connection = forms.IntegerField(required=True)
    frequency_of_clearance_of_waste_containers = forms.IntegerField(required=True)
    class Meta:
        model = Rapid_Slum_Appresal
        fields = (
        'slum_name',
        'approximate_population',
        'toilet_cost',
        'toilet_seat_to_persons_ratio'
        ,'percentage_with_an_individual_water_connection' 
        ,'frequency_of_clearance_of_waste_containers'
        ,'image1' 
        ,'image2'
        ,'image3' 
        ,'image4'
        )
    def clean_slum_name(self):
        slum_name = self.cleaned_data.get('slum_name')
        if slum_name is None:
            raise forms.ValidationError("This Field is required")
        return slum_name     
    
   
class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

