from django.shortcuts import render
from master.models import Survey
import urllib2
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from collections import OrderedDict
from itertools import chain


# Create your views here.


@csrf_exempt
def querydashboard(request):
	SurveyObject = Survey.objects.all()
	return render(request,'querydashboard.html',{'SurveyObject':SurveyObject})

@csrf_exempt
def surveyformlist(request):
    SurveyObject = Survey.objects.all()
    idArray = []
    nameArray = []   
    for i in SurveyObject:
        #print ("name", i.name)
        #print ("city",i.city.name.city_name)
        #print ("survey_type",i.survey_type)
        #print ("kobotool_survey_id", i.kobotool_survey_id)
        #print ("kobotool_survey_url", i.kobotool_survey_url)
        #print "*************"
        nameArray.append(str(i.name))
        idArray.append(i.kobotool_survey_id)
    data ={}
    data = { 'idArray'  : idArray,
             'nameArray': nameArray
           }
    return HttpResponse(json.dumps(data),content_type='application/json')




def trav2(node,name):
    #print name
    if node["type"] == "group" or node["type"] == "repeat":
        #print node
        return list(chain.from_iterable([trav2(child,name + "/" +  child["name"]) for child in node['children']]))
    else:
        node ['group'] = name
        return [node]



@csrf_exempt
def questionlist(request):
    formid = request.POST['id']
    print "formid\n"
    print formid
    data = {}
    data=datalist(formid)
    return HttpResponse(json.dumps(data),content_type='application/json')







def dictdata(data):
    #convert childrens to dictionary for parsing
    data['children'] = dict((str(topic['name']), topic) for topic in data['children'])

    for k,v in data['children'].items():
        if 'children' in v:
            if isinstance(v['children'], list):
                v = dictdata(v)
    return data


def trav(node):
    #Traverse uptill the child node and add to list
    if 'type' in node and node['type'] == "group" or node['type'] == "repeat":
        return list(chain.from_iterable([trav(child) for child in node['children']]))
    else:
        return [node]

def trav2(node,name):
    #print name
    if node["type"] == "group" or node["type"] == "repeat":
        #print node
        return list(chain.from_iterable([trav2(child,name + "/" +  child["name"]) for child in node['children']]))
    else:
        node ['group'] = name
        return [node]

def printq(node):
    list(chain.from_iterable([trav(child) for child in node['children']]))






def datalist(formid):
    print formid
    urlv = "http://192.168.2.6:8001/api/v1/forms/27/form.json"
    #urlv = "http://192.168.0.55:8001/api/v1/data/27?format=json"
    print ("Sending Request to",urlv)
    kobotoolbox_request = urllib2.Request(urlv)
    kobotoolbox_request.add_header('Authorization',"OAuth2 a0028f740988d80cbe670f24a9456d655b8dd419")
    res = urllib2.urlopen(kobotoolbox_request)
    html = res.read()
    formdict = json.loads(html)
    node = []
    dictarray =[]
    for dictarrayelement in formdict["children"]:
        if dictarrayelement['type'] == "group" or dictarrayelement['type']== "select one":
            node.append(trav2(dictarrayelement,dictarrayelement["name"]))
            dictarray.append(dictdata(dictarrayelement))
    print (node[3])
    node.pop()
    print len(node)
    questions = []
    for group in node:
        for question in group:
            questiondict = {}
            try:
                print "Question"
                print "####################"
                print question["label"]
                print question["name"]
                print question["group"]
                questiondict={"value":question["label"],"key":question["group"]}
                try:
                    print "Options of Questions"
                    options = []
                    for optionskey,optionsvalue in (question["children"]).items():
                        optiondict ={}
                        optiondict = {"value":optionsvalue["label"],"key":optionsvalue["name"]}
                        print (optionsvalue["label"],optionsvalue["name"])
                        options.append(optiondict)
                    questiondict["options"] = options
                except:
                    pass
                questions.append(questiondict)
                print "***********************************"
            except:
                pass
    #print questions
    form = {}
    form["form"] = questions
    print form
    return form




@csrf_exempt
def optionlist(request):
    print "I am optionlist"
    print "request"
    print request
    formid = request.POST['formkey']
    print "formid"
    print formid    
    questionname = request.POST['questionname'] 
    print "questionname"
    print questionname
    data = {}
    data=datalist(formid)
    print "#########################################"
    print "########################################"
    print type(data)
    print "questionname"
    print questionname
    questionlist = data["form"]
    optionlist = []
    for i in questionlist:
        try:
            if(i["value"]==questionname):
                print i["options"]
                optionlist = i["options"]
        except:
            pass 
    print optionlist               
    return HttpResponse(json.dumps(optionlist),content_type='application/json')


@csrf_exempt
def getformdata(request):
    print "$$$$$$$$$$$$$$$$$$$$$$$$$$$"
    data = []
    try:
        #print request.POST['data']
        data = json.loads(request.POST['data'])
        print type(data)
        #print json.loads(request.POST['data'])['1']
    except Exception as e:
        print e
    fdata=retrivedata(data) 
    print"fdata\n" 
    print fdata          
    return HttpResponse(json.dumps(fdata),content_type='application/json')



def retrivedata(data):
    print "printing data"
    formid = 0
    urlstring = "{"
    filterliststring = "&fields=["
    for i in data:
        Optionslist = []
        filterlists = [
        ]
        i['formid'] =  formid
        filterlists = i["filterlists"]
        print "filterlists"
        print "filterlists"
        print filterlists  
        Optionslist = i['Question'][0]['Options'] 
        if len(Optionslist) > 0:
            print "Optionslist length is greater than 0"
            for optionname in Optionslist:
                urlstring += '"' + i['Question'][0]['Questionid'] +'"'+ ":" + '"'+ optionname + '"' + "," 
        if len(filterlists) > 0:            
            for filterlist in filterlists:
                for key, value in filterlist.iteritems(): 
                    filterliststring += '"' + key + '"' +','         
    print "I am here too"                     
    print "I am here"                          
    print "urlstring"
    urlstring = urlstring[:-1]
    print urlstring
    urlstring = urlstring + "}"
    print filterliststring
    defaultfilterliststring = ["group_ce0hf58/Selct_city","group_ce0hf58/house_no","group_ye18c77/group_ud4em45/adhar_card_number"]
    for i in defaultfilterliststring:
        filterliststring = filterliststring + '"' + i + '"' + "," 
    filterliststring = filterliststring[:-1]
    print filterliststring
    filterliststring = filterliststring + "]"
    print "filterliststring"
    print filterliststring
    formid = 27
    urlv = "http://192.168.2.6:8001/api/v1/data/" + str(formid) + "?query=" +  urlstring + filterliststring         
    #urlv = "http://192.168.0.105:8001/api/v1/data/27?query={"Type_of_structure_occupancy": "01","group_ce0hf58/Selct_city":"3789"}" 
    print ("Sending Request to",urlv)
    kobotoolbox_request = urllib2.Request(urlv)
    kobotoolbox_request.add_header('Authorization',"OAuth2 a0028f740988d80cbe670f24a9456d655b8dd419")
    res = urllib2.urlopen(kobotoolbox_request)
    html = res.read()
    formdatadict = json.loads(html)
    print len(formdatadict)  
    print formdatadict
    return formdatadict