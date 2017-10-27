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


def datalist(formid):
    urlv = "http://192.168.0.55:8001/api/v1/forms/27/form.json"
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
    node.pop()
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
    form = {}
    form["form"] = questions
    print form
    return form
     
@csrf_exempt
def questionlist(request):
    data = {}
    data=mn()
    return HttpResponse(json.dumps(data),content_type='application/json')

def dd():
    urlv = "http://192.168.0.55:8001/api/v1/forms/27/form.json"
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
    print questions






import urllib2
import json
from collections import OrderedDict
from itertools import chain


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

def ll():
    urlv = "http://192.168.0.55:8001/api/v1/forms/27/form.json"
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
    print questions
    form = {}
    form["form"] = questions
    print json.dumps(form)





def mn():
    urlv = "http://192.168.0.55:8001/api/v1/forms/27/form.json"
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
    print questions
    form = {}
    form["form"] = questions
    return form
