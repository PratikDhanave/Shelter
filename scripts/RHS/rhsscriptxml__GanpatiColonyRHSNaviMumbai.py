from xml.dom.minidom import Document
import copy
from pymongo import MongoClient
import json
import uuid
import os
import sqlite3
from datetime import datetime
from dateutil import parser
import time
import re

"""
#Sitaram Machine RHS Samtanagar
xform_id_string="acM2J5uMF6NT5Xioccy4r3_MFvQzhQ"
versioncode="vrgvEhe9zqs4mBjf8kMSps"
formhub_id="7f169b532533486081eff91aa591ac86"
userform_id="softcorner_acM2J5uMF6NT5Xioccy4r3_MFvQzhQ"

"""

#my Machine
xform_id_string="aEE5T6NgZAcpqhDSEd5QLJ_ue7juEi"
versioncode="vntFj3rYntYQUPbyDuTWaj"
formhub_id="6b019e5460f241b083f73ac0c112d1db"
userform_id="softcorner_aEE5T6NgZAcpqhDSEd5QLJ_ue7juEi"

"""
#sheltermachine
xform_id_string="akfz8qCaUdhQDcjqVEGADi"
versioncode="vnfRxPHHu9k2Y9xd6HNDt8"
formhub_id="bc92c6c6eecf44f69e9c9a39a624077a"
userform_id="softcorner_akfz8qCaUdhQDcjqVEGADi"
"""

"""
#Live
xform_id_string="aLaMKLSPygDyE5BmBzhUWz"
versioncode="vHPPjX2prBrs695YAWPmH7"
formhub_id="5284bf8321de44e78fd46f5629083975"
userform_id="shelter_aLaMKLSPygDyE5BmBzhUWz"
"""

client = MongoClient('mongodb://127.0.0.1:27017/')

#databse name
mongodb = client['shelterlive']

house_no=""
admin_no=""
slum_no=""
city_id=""
id_id = " "

listvar={}


folder = "/home/softcorner/ShelterAssociates/src/scripts/RHS/xmlfiles/GanpatiColonyRHSNaviMumbai/"
sqlitepath="/storage/emulated/0/odk/instances/RHS Final_2016-12-09_11-00-10/"


def printdata():
    listvar = {}
    count = 0
    id_id = ""
    demo=0
    try:
        dataval=mongodb.instances.find({"_xform_id_string" :"aeg4mkNhppRkpdrJzrCSZm"})
        for data in dataval:
            count = count + 1
            listvar={}
            listvar['group_ce0hf58']= {}
            listvar['formhub'] = {}
            listvar['meta'] = {}
            listvar['group_ye18c77'] = {}
            listvar['group_ye18c77']['group_ud4em45'] = {}
            listvar['group_ye18c77']['group_yw8pj39'] = {}
            for key,value in data.items():
                if key == 'group_jg6ts57/city_name':#1
                    listvar['group_ce0hf58'].update({'city':str("7149")})
                    city_id = str("3789")
                elif key == 'group_jg6ts57/select_administrative_ward_nam':#2
                    listvar['group_ce0hf58'].update({'admin_ward':str('NM02')})
                    admin_no = str("PC03")
                elif key == 'group_jg6ts57/select_slum':#3
                    listvar['group_ce0hf58'].update({'slum_name':str(value)})
                    slum_no= str(value)
                elif key == 'group_jg6ts57/date_of_rapid_household_survey':#4
                    listvar['group_ce0hf58'].update({'date_of_rhs':str(value)})
                elif key =='group_jg6ts57/Name_of_surveyor_s_who_collec_001':#5
                    listvar['group_ce0hf58'].update({'name_of_surveyor_who_collected_rhs_data':str(value)})
                elif key =='group_jg6ts57/house_number':#6
                    listvar['group_ce0hf58'].update({'house_no':str(value)})
                    house_no=str(specialcharremover(str(value)))
                elif key == 'type_of_house_occupancy':#7
                    listvar['group_ce0hf58'].update({'Type_of_structure_occupancy':str(value)})
                elif key == 'group_xb9nq26/group_do8xg48/what_is_the_full_name_of_the_f':#8
                    listvar['group_ye18c77']['group_ud4em45']['what_is_the_full_name_of_the_family_head_']={}
                    listvar['group_ye18c77']['group_ud4em45']['what_is_the_full_name_of_the_family_head_']=str(value)
                elif key == 'group_xb9nq26/group_do8xg48/mobile_number':#9
                    listvar['group_ye18c77']['group_ud4em45']['mobile_number']={}
                    listvar['group_ye18c77']['group_ud4em45']['mobile_number']=str(value)
                elif key == 'group_xb9nq26/group_do8xg48/aadhar_card_number':#10
                    listvar['group_ye18c77']['group_ud4em45']['adhar_card_number']={}
                    listvar['group_ye18c77']['group_ud4em45']['adhar_card_number']=str(value)
                elif key == 'group_xb9nq26/group_io6zh11/type_of_structure_of_the_house':#11
                    listvar['group_ye18c77']['group_yw8pj39']['what_is_the_structure_of_the_house']=str(specialcharremover(str(value)))
                elif key == 'group_xb9nq26/group_io6zh11/ownership_status':#12
                    if value =='03':
                        listvar['group_ye18c77']['group_yw8pj39']['what_is_the_ownership_status_of_the_house']=str('01')
                    else:
                        listvar['group_ye18c77']['group_yw8pj39']['what_is_the_ownership_status_of_the_house']=str(specialcharremover(str(value)))
                elif key == 'group_xb9nq26/group_io6zh11/no_of_family_fembers':#13
                    listvar['group_ye18c77']['group_yw8pj39']['number_of_family_members']=str(specialcharremover(str(value)))
                elif key == 'group_xb9nq26/group_io6zh11/do_you_have_girl_child_under_a':#14
                    listvar['group_ye18c77']['group_yw8pj39']['Do_you_have_a_girl_child_under']=str(specialcharremover(str(value)))
                elif key == 'group_xb9nq26/group_io6zh11/if_yes_how_many':#15
                    listvar['group_ye18c77']['group_yw8pj39']['if_yes_how_many_']=str(specialcharremover(str(value)))
                elif key == 'group_xb9nq26/group_io6zh11/house_area_in_sq_ft':#16
                    listvar['group_ye18c77']['group_yw8pj39']['house_area_in_sq_ft']=str(specialcharremover(str(value)))
                elif key =='group_xb9nq26/group_io6zh11/current_place_of_defecation_t':#17
                    if value == '01':
                        listvar['group_ye18c77']['group_yw8pj39']['Current_place_of_defecation_toilet']=str("01")
                    elif value == '02':
                        listvar['group_ye18c77']['group_yw8pj39']['Current_place_of_defecation_toilet']=str("03")
                    elif value == '03':
                        listvar['group_ye18c77']['group_yw8pj39']['Current_place_of_defecation_toilet']=str("04")
                    elif value == '04':
                        listvar['group_ye18c77']['group_yw8pj39']['Current_place_of_defecation_toilet']=str("07")
                    elif value == '05':
                        listvar['group_ye18c77']['group_yw8pj39']['Current_place_of_defecation_toilet']=str("05")
                elif key =='group_xb9nq26/group_io6zh11/where_the_individual_toilet_is':#18
                    if value == '09':
                        listvar['group_ye18c77']['group_yw8pj39']['where_the_individual_toilet_is_connected_to_']=value
                    else:
                        listvar['group_ye18c77']['group_yw8pj39']['where_the_individual_toilet_is_connected_to_']=value
                elif key == 'group_xb9nq26/group_io6zh11/type_of_water_connection':#19
                    listvar['group_ye18c77']['group_yw8pj39']['type_of_water_connection']=str(specialcharremover(str(value)))
                elif key == 'group_xb9nq26/group_io6zh11/facility_of_waste_collection':#20
                    checker=str(value.split(" ")[0])
                    if checker == '01':
                        listvar['group_ye18c77']['group_yw8pj39']['facility_of_waste_collection']=str("03")
                        print "03"
                    elif checker == '02':
                        listvar['group_ye18c77']['group_yw8pj39']['facility_of_waste_collection']=str("02")
                        print "02"
                    elif checker =="03":
                        listvar['group_ye18c77']['group_yw8pj39']['facility_of_waste_collection']=str("03")
                        print "03"
                    elif checker == '04':
                        listvar['group_ye18c77']['group_yw8pj39']['facility_of_waste_collection']=str("03")
                        print "04"
                    elif checker == '05':
                        listvar['group_ye18c77']['group_yw8pj39']['facility_of_waste_collection']=str("04")
                        print "04"
                    elif checker =="06":
                        listvar['group_ye18c77']['group_yw8pj39']['facility_of_waste_collection']=str("05")
                        print "05"
                    elif checker == '07':
                        listvar['group_ye18c77']['group_yw8pj39']['facility_of_waste_collection']=str("06")
                        print "06"
                    elif checker =="08":
                        print "Hiiiiiiiiiiiiiiiiiiiiiiiiiiii"
                        listvar['group_ye18c77']['group_yw8pj39']['facility_of_waste_collection']=str("07")
                elif key == 'group_xb9nq26/group_io6zh11/interested_in_individual_toile':#21
                    listvar['group_ye18c77']['group_yw8pj39']['Are_you_interested_in_individu']=str(specialcharremover(str(value)))
                elif key == 'group_xb9nq26/group_io6zh11/if_yes_why':#22
                    listvar['group_ye18c77']['group_yw8pj39']['if_yes_why_']=str(specialcharremover(str(value)))
                elif key =='group_xb9nq26/group_io6zh11/if_no_why':#23
                    listvar['group_ye18c77']['group_yw8pj39']['if_no_why_']=str(specialcharremover(str(value)))
                elif key =='group_xb9nq26/group_io6zh11/type_of_toilet_preference':#24
                    listvar['group_ye18c77']['group_yw8pj39']['type_of_toilet_preference']=str(specialcharremover(str(value)))
                elif key =='group_xb9nq26/group_io6zh11/have_you_applied_or_individual':#25
                    listvar['group_ye18c77']['group_yw8pj39']['Have_you_applied_for_indiviual']=str(specialcharremover(str(value)))
                elif key == 'group_xb9nq26/group_io6zh11/how_many_installments_have_yo':#26
                    listvar['group_ye18c77']['group_yw8pj39']['How_many_installements_have_yo']=str(value)
                elif key =="formhub/uuid":#27
                    listvar['formhub']['uuid']= {}
                    listvar['formhub']['uuid']=formhub_id
                elif key== "meta/instanceID":#28
                    listvar['meta']['instanceID']= {}
                    listvar['meta']['instanceID']= "uuid:" + str(uuid.uuid4())
                elif key =="__version__":#29
                    listvar['__version__']={}
                    listvar['__version__']=versioncode
                elif key=="_userform_id":#30
                    listvar['_userform_id']={}
                    listvar['_userform_id']=userform_id
                elif key== "_id":#31
                    id_id = value
                elif key == 'end':#32
                    listvar['end']={}
                    listvar['end']=value
                elif key =='start':#33
                    listvar['start']={}
                    listvar['start']=value
                elif key =='_submission_time':#34
                    listvar['_submission_time']={}
                    listvar['_submission_time']=value
                elif key=="_xform_id_string":#35
                    listvar['_xform_id_string']= {}
                    listvar['_xform_id_string']=str(xform_id_string)
                elif key == '_submitted_by':#36
                    listvar['_submitted_by']={}
                    listvar['_submitted_by']=value
            xmldata=""
            xmldata = dict2xml({xform_id_string : listvar})
            xmlfinal=""
            xmlfinal=str(xmldata.display()).replace('<'+xform_id_string+'>','<'+xform_id_string+'  id="'+xform_id_string+'" version="'+versioncode+'">').replace('<_xform_id_string/>','')
            listvar = {}
            filename=str("RHS_"+city_id+"_"+admin_no+"_"+slum_no+"_"+house_no+"_"+ str(id_id)+".xml")
            with open(folder +"/"+filename, 'w') as f:
                f.write(xmlfinal)
                f.close()
    except Exception as ex:
        print "hhhhhhhhhhhhh",ex


def specialcharremover(stringv):
    stringval = re.sub('[^A-Za-z0-9" "]+', '', stringv)
    return str(stringval)

class dict2xml(object):
    #print type(doc)
    def __init__(self, structure):
        if len(structure) == 1:
            rootName    = str(structure.keys()[0])
	    self.doc = Document()
            self.root   = self.doc.createElement(rootName)
            self.doc.appendChild(self.root)
            self.build(self.root, structure[rootName])

    def build(self, father, structure):
        if type(structure) == dict:
            for k in structure:
                tag = self.doc.createElement(k)
                father.appendChild(tag)
                self.build(tag, structure[k])

        elif type(structure) == list:
            grandFather = father.parentNode
            tagName     = father.tagName
            grandFather.removeChild(father)
            for l in structure:
                tag = self.doc.createElement(tagName)
                self.build(tag, l)
                grandFather.appendChild(tag)

        else:
            data    = str(structure)
            tag     = self.doc.createTextNode(data)
            father.appendChild(tag)

    def display(self):
        #print self.doc.toprettyxml(indent="  ")
        xml_data1=""
	xml_data1=self.doc.toprettyxml(indent="  ")
	return xml_data1

#/********************************/
valuelist=[]
def jsonformat(jsonvar):
    list1={}
    for n,value in jsonvar.items():
	    str_split=n.split('/')
	    if type(value) ==list:
		if len(str_split)==2:
		    for ln in value:
			list2={}
	        	for key,lin in ln.items():
	    	    	    list_split=str(key).split('/')
            	     	    list2.update({list_split[2]:lin})
			valuelist.append(list2)

		    if str_split[0] not in list1:
		        list1[str_split[0]]={}
		    if str_split[1] not in list1[str_split[0]]:
		        list1[str_split[0]][str_split[1]]={}
		        list1[str_split[0]].update({str_split[1]:valuelist})

	    else:

		if len(str_split)==3:
		    if str_split[0] not in list1:
		        list1[str_split[0]]={}
		    if str_split[1] not in list1[str_split[0]]:
		        list1[str_split[0]][str_split[1]]={}
		    list1[str_split[0]][str_split[1]].update({str_split[2]:value})
		if len(str_split)==2:
		    if str_split[0] not in list1:
		        list1[str_split[0]]={}
		    list1[str_split[0]].update({str_split[1]:value})
		if len(str_split)==1:
		    if str_split[0] not in list1:
		        list1[str_split[0]]={}
		    if str(str_split[0]) != "_xform_id_string":
		        list1[str_split[0]]=value

    return list1

#/********************************/

def func(keyls):
	list_data=[]
	print keyls.keys()[0],keyls.values()[0]
	dbslum(keyls.keys()[0],keyls.values()[0])
	extraTypeSlum(keyls.keys()[0],keyls.values()[0])




def main():
    printdata()


if __name__ == '__main__':
    main()
