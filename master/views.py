#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The Django Views Page for master app"""
import json
import urllib2

from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseForbidden
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView

from master.models import Survey, CityReference, Rapid_Slum_Appresal, Slum, ExampleModel
from master.forms import SurveyCreateForm, Rapid_Slum_AppresalForm, ImageUploadForm

from django.views.generic.base import View
from wkhtmltopdf.views import PDFTemplateResponse
from django.shortcuts import render

@staff_member_required

def index(request):
    """Renders the index template in browser"""
    template = loader.get_template('index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


class SurveyListView(ListView):
    """Renders the Survey View template in browser"""
    template_name = 'SurveyListView.html'
    model = Survey

    def get_queryset(self):
        try:
            filter_input = self.kwargs['name']
        except KeyError:
            filter_input = ''
        if filter_input != '':
            object_list = self.model.objects.filter(name__icontains=filter_input)
        else:
            object_list = self.model.objects.all()
        return object_list


class SurveyCreateView(FormView):
    """Fetches and renders the Add New Survey Mapping template in browser"""
    template_name = 'SurveyCreate_form.html'
    form_class = SurveyCreateForm
    success_url = 'SurveyCreate/'

    def dispatch(self, request, *args, **kwargs):
        """Signal Dispatcher"""
        try:
            if kwargs['survey']:
                self.id = kwargs['survey']
        except KeyError:
            print 'Error'
        return super(SurveyCreateView, self).dispatch(request, *args,
                                                      **kwargs)

    def get_context_data(self, **kwargs):
        """Returns a dictionary(json data format)"""
        context_data = super(SurveyCreateView,
                             self).get_context_data(**kwargs)
        try:
            if self.id:
                self.surveydata = Survey.objects.get(id=self.id)
                context_data['form'] = self.form_class(initial={
                    'name': self.surveydata.name,
                    'description': self.surveydata.description,
                    'city': self.surveydata.city,
                    'survey_type': self.surveydata.survey_type,
                    'analysis_threshold': self.surveydata.analysis_threshold,
                    'kobotool_survey_id': self.surveydata.kobotool_survey_id,
                    'survey': self.surveydata.id,
                    })
        except RuntimeError:
            print 'get_context_data Error'
        return context_data

    def get_form_kwargs(self):
        """'Get' request for form data"""
        kwargs = super(SurveyCreateView, self).get_form_kwargs()
        try:
            kwargs['survey'] = self.id
        except AttributeError:
            print 'get_form_kwargs Error'
        return kwargs

    def form_valid(self, form):
        """Actions to perform if form is valid"""
        form.save()
        return super(SurveyCreateView, self).form_valid(form)

    def form_invalid(self, form):
        """Actions to perform if form is invalid"""
        return super(SurveyCreateView, self).form_invalid(form)

    def get_success_url(self):
        """If form is valid -> redirect to"""
        return reverse('SurveyCreate')


def survey_delete_view(survey):
    """Delete Survey Object"""
    obj = Survey.objects.get(id=survey)
    if obj:
        obj.delete()
        message = 'Success'
    else:
        message = 'Failure'
    data = {}
    data['message'] = message
    return HttpResponseRedirect('/admin/surveymapping/')

@csrf_exempt
def search(request):
    """Autofill add city form fields based on City ID"""
    sid = request.POST['id']
    cityref = CityReference.objects.get(id=sid)
    data_dict = {
        'city_code': str(cityref.city_code),
        'district_name': str(cityref.district_name),
        'district_code': str(cityref.district_code),
        'state_name': str(cityref.state_name),
        'state_code': str(cityref.state_code),
        }
    return HttpResponse(json.dumps(data_dict),
                        content_type='application/json')


class mypdfview(View):#url="http://kc.shelter-associates.org/api/v1/data/161?format=json" #url= "http://45.56.104.240:8001/api/v1/data/161?format=json"
    url= "http://45.56.104.240:8001/api/v1/data/161?format=json"
    req = urllib2.Request(url)
    req.add_header('Authorization', 'OAuth2 a0028f740988d80cbe670f24a9456d655b8dd419')
    resp = urllib2.urlopen(req)
    content = resp.read()
    data = json.loads(content)
    p=data[0]
    result=p['_attachments']
    slumname ="PuneSlum"
    datadict = {slumname :"PuneSlum"}
    SurveyNumber = 1
    img ="http://45.56.104.240:8001/media/"+result[0]['filename']
    template='report.html'#print datadict[slumname]
    context= {'img':img,'data':data,'datadict':datadict}
    def get(self, request):
        response = PDFTemplateResponse(request=request,
                                        template=self.template,
                                        filename="hello.pdf",
                                        context= self.context,
                                       show_content_in_browser=False,
                                       cmd_options={'margin-top': 50,},
                                       )
        return response


def delete(request, person_id):
    p = Person.objects.get(pk=person_id)
    p.delete()
    return HttpResponseRedirect('/')
    

def display(request):
    R = Rapid_Slum_Appresal.objects.all()
    for i in R:
        print i.approximate_population
    t = loader.get_template('display4.html')
    c = RequestContext(request, {'R':R})
    return HttpResponse(t.render(c))


"""
def insert(request):
    print request
    if request.method == 'POST':
        R = Rapid_Slum_Appresal(
            slum_name = request.POST['slum_name'],
            approximate_population= request.POST['approximate_population'],
            toilet_cost=request.POST['toilet_cost'],            
            toilet_seat_to_persons_ratio = request.POST['toilet_seat_to_persons_ratio'],
            percentage_with_an_individual_water_connection = request.POST['percentage_with_an_individual_water_connection'],
            frequency_of_clearance_of_waste_containers = request.POST['frequency_of_clearance_of_waste_containers'],
            image1=request.POST['Image1'],
            image2=request.POST['Image2'],
            image3=request.POST['Image3'],
            image4=request.POST['Image4']            
        )
        R.save()
    t = loader.get_template('insert.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))
"""

"""

def edit(request,Rapid_Slum_Appresal_id):
    R = Rapid_Slum_Appresal.objects.get(pk=Rapid_Slum_Appresal_id)
    form = Rapid_Slum_AppresalForm()
    print type(form)
    print R.slum_name
    print R.approximate_population
    print R.toilet_cost
    print R.toilet_seat_to_persons_ratio
    print R.percentage_with_an_individual_water_connection
    print R.frequency_of_clearance_of_waste_containers
    print R.image1
    print R.image2
    print R.image3
    print R.image4
    
    if request.method == 'POST':
        slum_name = Slumref
        approximate_population= request.POST['approximate_population']
        toilet_cost=request.POST['toilet_cost']           
        toilet_seat_to_persons_ratio = request.POST['toilet_seat_to_persons_ratio']
        percentage_with_an_individual_water_connection = request.POST['percentage_with_an_individual_water_connection']
        frequency_of_clearance_of_waste_containers = request.POST['frequency_of_clearance_of_waste_containers']
        image1=request.POST['Image1']
        image2=request.POST['Image2']
        image3=request.POST['Image3']
        image4=request.POST['Image4']  
        R.save()

    if request.method=='GET':
        slum_name = R.slum_name
        approximate_population= R.approximate_population
        toilet_cost= R.toilet_cost           
        toilet_seat_to_persons_ratio = R.toilet_seat_to_persons_ratio
        percentage_with_an_individual_water_connection = R.percentage_with_an_individual_water_connection
        frequency_of_clearance_of_waste_containers = R.frequency_of_clearance_of_waste_containers
        image1 = R.image1
        image2 = R.image2
        image3 = R.image3
        image4 = R.image4  
    
    return render(request, '1.html', {'form': form}) 

"""
"""

    t = loader.get_template('insert.html')
    c = RequestContext(request, {
        'Rapid_Slum_Appresal': R
    })

    return HttpResponse(t.render(c))

    """

"""
def edit(request,Rapid_Slum_Appresal_id):
    R = Rapid_Slum_Appresal.objects.get(pk=Rapid_Slum_Appresal_id)#Slumref= Slum.objects.get(id=R.slum_name)
    if request.method == 'POST':
        slum_name =  Slum.objects.get(id=request.POST['slum_name']),
        approximate_population= request.POST['approximate_population']
        toilet_cost=request.POST['toilet_cost']           
        toilet_seat_to_persons_ratio = request.POST['toilet_seat_to_persons_ratio']
        percentage_with_an_individual_water_connection = request.POST['percentage_with_an_individual_water_connection']
        frequency_of_clearance_of_waste_containers = request.POST['frequency_of_clearance_of_waste_containers']
        image1=request.POST['Image1']
        image2=request.POST['Image2']
        image3=request.POST['Image3']
        image4=request.POST['Image4']  
        R.save()
    t = loader.get_template('insert.html')
    c = RequestContext(request, {
        'Rapid_Slum_Appresal': R
    })
    return HttpResponse(t.render(c))
"""


"""
def ins(request):
    if request.method == 'POST':
        form = Rapid_Slum_AppresalForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = Rapid_Slum_AppresalForm()

    return render(request, '1.html', {'form': form})

"""

class RapidSlumAppresalView(FormView):
    template_name = '2.html'
    form_class = Rapid_Slum_AppresalForm
    def post(self, request):
        print request.POST
        print form_class.is_valid()
        Slumref = Slum.objects.get(id=request.POST['slum_name'])
        R = Rapid_Slum_Appresal(
            slum_name = Slumref ,
            approximate_population= request.POST['approximate_population'],
            toilet_cost=request.POST['toilet_cost'],            
            toilet_seat_to_persons_ratio = request.POST['toilet_seat_to_persons_ratio'],
            percentage_with_an_individual_water_connection = request.POST['percentage_with_an_individual_water_connection'],
            frequency_of_clearance_of_waste_containers = request.POST['frequency_of_clearance_of_waste_containers'],
            image1=request.POST['image1'],
            image2=request.POST['image2'],
            image3=request.POST['image3'],
            image4=request.POST['image4']            
        )
        R.save()
        return HttpResponse('done')





from django.shortcuts import render, redirect
from django.views.generic.base import View



class ClassBasedView(View):
    def get(self,request,Rapid_Slum_Appresal_id):
        R = Rapid_Slum_Appresal.objects.get(pk=Rapid_Slum_Appresal_id)#Slumref= Slum.objects.get(id=R.slum_name) 
        form = Rapid_Slum_AppresalForm(instance= R)
        context = {'form': form}
        return render(request, '3.html', context)

    def post(self, request):
        form = Rapid_Slum_AppresalForm()
        Slumref = Slum.objects.get(id=request.POST['slum_name'])
        form = Rapid_Slum_AppresalForm()
        R = Rapid_Slum_Appresal(
            slum_name = Slumref ,
            approximate_population= request.POST['approximate_population'],
            toilet_cost=request.POST['toilet_cost'],            
            toilet_seat_to_persons_ratio = request.POST['toilet_seat_to_persons_ratio'],
            percentage_with_an_individual_water_connection = request.POST['percentage_with_an_individual_water_connection'],
            frequency_of_clearance_of_waste_containers = request.POST['frequency_of_clearance_of_waste_containers'],
            image1=request.POST['image1'],
            image2=request.POST['image2'],
            image3=request.POST['image3'],
            image4=request.POST['image4']            
        )
        R.save()
        return HttpResponse('done')

def edit(request,Rapid_Slum_Appresal_id):
    R = Rapid_Slum_Appresal.objects.get(pk=Rapid_Slum_Appresal_id)#Slumref= Slum.objects.get(id=R.slum_name) 
    form = Rapid_Slum_AppresalForm(instance= R)
    a=form.is_valid()
    print a
    if request.method == 'POST':
        slum_name =  Slum.objects.get(id=request.POST['slum_name']),
        approximate_population= request.POST['approximate_population']
        toilet_cost=request.POST['toilet_cost']           
        toilet_seat_to_persons_ratio = request.POST['toilet_seat_to_persons_ratio']
        percentage_with_an_individual_water_connection = request.POST['percentage_with_an_individual_water_connection']
        frequency_of_clearance_of_waste_containers = request.POST['frequency_of_clearance_of_waste_containers']
        image1=request.POST['image1']
        image2=request.POST['image2']
        image3=request.POST['image3']
        image4=request.POST['image4']  
        R.save()
        print request.POST
    return render(request, '3.html', {'form': form})










"""
@csrf_exempt
def ins(request):
    print request.POST
    form = Rapid_Slum_AppresalForm(request.POST) 
    if request.method == 'POST':
        if form.is_valid():
            Slumref = Slum.objects.get(id=request.POST['slum_name'])
            print Slumref
            print "I am in valid Block"
            R = Rapid_Slum_Appresal(
                slum_name = Slumref,
                approximate_population= request.POST['approximate_population'],
                toilet_cost=request.POST['toilet_cost'],            
                toilet_seat_to_persons_ratio = request.POST['toilet_seat_to_persons_ratio'],
                percentage_with_an_individual_water_connection = request.POST['percentage_with_an_individual_water_connection'],
                frequency_of_clearance_of_waste_containers = request.POST['frequency_of_clearance_of_waste_containers'],
                image1=request.POST['image1'],
                image2=request.POST['image2'],
                image3=request.POST['image3'],
                image4=request.POST['image4']            
            )
            R.save()
            return  HttpResponseRedirect('/admin/ins')
        else:
            print "I am in invalid Block"
            print form.errors
                       
    else:
        form = Rapid_Slum_AppresalForm()
    return render(request, '2_boot.html', {'form': form})

"""

def inst(request):
    R = Rapid_Slum_Appresal()
    form = Rapid_Slum_AppresalForm(request.POST,instance=R) 
    print request.POST
    if request.method == 'POST':
        Slumref = Slum.objects.get(id=request.POST['slum_name'])
        print Slumref
        R = Rapid_Slum_Appresal(
                slum_name = Slumref,
                approximate_population= request.POST['approximate_population'],
                toilet_cost=request.POST['toilet_cost'],            
                toilet_seat_to_persons_ratio = request.POST['toilet_seat_to_persons_ratio'],
                percentage_with_an_individual_water_connection = request.POST['percentage_with_an_individual_water_connection'],
                frequency_of_clearance_of_waste_containers = request.POST['frequency_of_clearance_of_waste_containers'],
                image1=request.POST['image1'],
                image2=request.POST['image2'],
                image3=request.POST['image3'],
                image4=request.POST['image4']            
            )
        R.save()
    return render(request, '2_boot.html', {'form': form})

"""

def insert(request):
    errors =[]
    form = Rapid_Slum_AppresalForm(request.POST,request.FILES)
    print request.POST
    print request.FILES
    if request.method == 'POST':
        form = Rapid_Slum_AppresalForm(request.POST,request.FILES)
        if form.is_valid():
            print "hello form is valid"            
            Slumref = Slum.objects.get(id=request.POST['slum_name'])
            R = Rapid_Slum_Appresal(
                slum_name = Slumref,
                approximate_population= request.POST['approximate_population'],
                toilet_cost=request.POST['toilet_cost'],            
                toilet_seat_to_persons_ratio = request.POST['toilet_seat_to_persons_ratio'],
                percentage_with_an_individual_water_connection = request.POST['percentage_with_an_individual_water_connection'],
                frequency_of_clearance_of_waste_containers = request.POST['frequency_of_clearance_of_waste_containers'],
                image1=request.FILES['image1'],
                image2=request.FILES['image2'],
                image3=request.FILES['image3'],
                image4=request.FILES['image4']            
            )
            R.save()
    return render(request, 'form.html', {'form': form,'errors':errors})

"""

def upload_pic(request):
    form = ImageUploadForm(request.POST, request.FILES)
    if request.method == 'POST':
        print request.POST
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            E =ExampleModel(model_pic=request.POST['image'])
            E.save()
            return HttpResponse('image upload success')
    return render(request, 'example.html', {'form': form})





def insert(request):
    if request.method == 'POST':
        form = Rapid_Slum_AppresalForm(request.POST,request.FILES)
        a =form.is_valid()
        print a
        if a is True:
            print "form is saved"
            form.save()
        else:
            print form.errors    
    else:
        form = Rapid_Slum_AppresalForm()        
    return render(request, 'boot_6.html', {'form': form})

