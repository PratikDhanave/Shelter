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
#db.instances.find({"_xform_id_string" :"aRfQkaXgucnaEVxSREBZHW"}).limit(1)
#db.instances.count({"_xform_id_string" :"aRfQkaXgucnaEVxSREBZHW"})
#db.instances.insert("name","address") values("AAA","Pune")
#db.instances.update({"_xform_id_string" :"aRfQkaXgucnaEVxSREBZHW"},{$set:{"_attachments":[]}},{multi:true})
#db.instances.remove( {"_id": 13 });
#/********************************/
#my
xform_id_string="a5iCPVYV2sjjJiWRvKGYkk"
versioncode="va5Nww2pctGvPAGYM77TPk"
formhub_id="966cb203b63c4f25b91d17fa1c27d505"
userform_id="softcorner_a5iCPVYV2sjjJiWRvKGYkk"


client = MongoClient('mongodb://127.0.0.1:27017/')

#databse name
mongodb = client['shelterlive']
jsonvar={}

house_no=""
admin_no=""
slum_no=""
city_id=""
id_id = ""
folder = "/home/softcorner/ShelterAssociates/src/scripts/RHS/xmlfiles/RapidHouseholdSurvey"
sqlitepath="/storage/emulated/0/odk/instances/RHS Final_2016-12-09_11-00-10/"


def printdata():
    count = 0
    id_id = ""
    demo=0
    try:
        dataval=mongodb.instances.find({"_xform_id_string" :"abowbPoPd9YqKp6Z2VnZqb"}).limit(1)
        for data in dataval:
            for key,value in data.items():
                try:
                    if key == 'group_ce0hf58/Selct_city':#1
                        jsonvar['group_ce0hf58/city']=str("3789")
                        city_id = str("3789")
                        slum_no= str(specialcharremover(str(value)))
                    elif key == 'group_ce0hf58/select_slum_of_admin_ward_c':#3
                        slum_no= str(specialcharremover(str(value)))
                        jsonvar['group_ce0hf58/slum_name']=str(specialcharremover(str(value)))
                    elif key == 'group_ce0hf58/select_slum_of_admin_e':#3
                        jsonvar['group_ce0hf58/slum_name']=str(specialcharremover(str(value)))
                        slum_no= str(specialcharremover(str(value)))
                    elif key == 'group_ce0hf58/select_slum_of_admin_f':#3
                        jsonvar['group_ce0hf58/slum_name']=str(specialcharremover(str(value)))
                        slum_no= str(specialcharremover(str(value)))
                    elif key == 'group_ce0hf58/Select_admin_ward':#2
                        if value == "03":
                            jsonvar['group_ce0hf58/admin_ward']=str("PC03")
                            admin_no = str("PC03")
                        elif value == "05":
                            jsonvar['group_ce0hf58/admin_ward']=str("PC05")
                            admin_no = str("PC05")
                        elif value == "06":
                            jsonvar['group_ce0hf58/admin_ward']=str("PC06")
                            admin_no = str("PC06")
                    elif key == 'group_ce0hf58/date_of_rhs':#4
                        jsonvar['group_ce0hf58/date_of_rhs']=value
                    elif key =='group_ce0hf58/name_of_surveyor_who_collected_rhs_data':#5
                        jsonvar['group_ce0hf58/name_of_surveyor_who_collected_rhs_data']=str(specialcharremover(str(value)))
                    elif key =='group_ce0hf58/house_no':#6
                        jsonvar['group_ce0hf58/house_no']=str(specialcharremover(str(value)))
                        house_no=str(specialcharremover(str(value)))
                    elif key == "group_ye18c77/group_yw8pj39/what_is_the_structure_of_the_house":#7
                        jsonvar['group_ye18c77/group_yw8pj39/what_is_the_structure_of_the_house']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_ud4em45/what_is_the_full_name_of_the_family_head_':#8
                        jsonvar['group_ye18c77/group_ud4em45/what_is_the_full_name_of_the_family_head_']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_ud4em45/mobile_number':#9
                        jsonvar['group_ye18c77/group_ud4em45/mobile_number']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_ud4em45/adhar_card_number':#10
                        jsonvar['group_ye18c77/group_ud4em45/adhar_card_number']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/what_is_the_ownership_status_of_the_house':#11
                        jsonvar['group_ye18c77/group_yw8pj39/what_is_the_ownership_status_of_the_house']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/number_of_family_members':#12
                        jsonvar['group_ye18c77/group_yw8pj39/number_of_family_members']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/Do_you_have_a_girl_child_under':#13
                        jsonvar['group_ye18c77/group_yw8pj39/Do_you_have_a_girl_child_under']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/if_yes_how_many_':#14
                        jsonvar['group_ye18c77/group_yw8pj39/if_yes_how_many_']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/house_area_in_sq_ft':#15
                        jsonvar['group_ye18c77/group_yw8pj39/house_area_in_sq_ft']=str(specialcharremover(str(value)))
                    elif key =='group_ye18c77/group_yw8pj39/Current_place_of_defecation_t':#16
                        jsonvar['group_ye18c77/group_yw8pj39/Current_place_of_defecation_toilet']=str(specialcharremover(str(value)))
                    elif key =='group_ye18c77/group_yw8pj39/where_the_individual_toilet_is_connected_to_':#17
                        jsonvar['group_ye18c77/group_yw8pj39/where_the_individual_toilet_is_connected_to_']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/type_of_water_connection':#18
                        jsonvar['group_ye18c77/group_yw8pj39/type_of_water_connection']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/facility_of_waste_collection':#19
                        jsonvar['group_ye18c77/group_yw8pj39/facility_of_waste_collection']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/Are_you_interested_in_individu':#20
                        jsonvar['group_ye18c77/group_yw8pj39/Are_you_interested_in_individu']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/if_yes_why_':#21
                        jsonvar['group_ye18c77/group_yw8pj39/if_yes_why_']=str(specialcharremover(str(value)))
                    elif key =='group_ye18c77/group_yw8pj39/if_no_why_':#22
                        jsonvar['group_ye18c77/group_yw8pj39/if_no_why_']=str(specialcharremover(str(value)))
                    elif key =='group_ye18c77/group_yw8pj39/type_of_toilet_preference':#23
                        jsonvar['group_ye18c77/group_yw8pj39/type_of_toilet_preference']=str(specialcharremover(str(value)))
                    elif key =='group_ye18c77/group_yw8pj39/Have_you_applied_for_indiviual':#24
                        jsonvar['group_ye18c77/group_yw8pj39/Have_you_applied_for_indiviual']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/How_many_installements_have_yo':#25
                        jsonvar['group_ye18c77/group_yw8pj39/How_many_installements_have_yo']=value
                    elif key == 'group_ye18c77/group_yw8pj39/does_any_member_of_your_family_go_for_open_defecation_':#26
                        jsonvar['group_ye18c77/group_yw8pj39/does_any_member_of_your_family_go_for_open_defecation_']=str(specialcharremover(str(value)))
                    elif key == 'Type_of_structure_occupancy':#27
                        jsonvar['group_ce0hf58/Type_of_structure_occupancy']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/when_did_you_receive_the_first_installment_date':#28
                            jsonvar['group_ye18c77/group_yw8pj39/when_did_you_receive_the_first_installment_date']=value
                    elif key == 'group_ye18c77/group_yw8pj39/when_did_you_receive_the_second_installment_date':#29
                            jsonvar['group_ye18c77/group_yw8pj39/when_did_you_receive_the_second_installment_date']=value
                    elif key == 'group_ye18c77/group_yw8pj39/what_is_thehave_status_of_toilet_under_sbm_':#30
                        jsonvar['group_ye18c77/group_yw8pj39/what_is_thehave_status_of_toilet_under_sbm_']=value
                    elif key == 'group_ye18c77/group_yw8pj39/Does_any_family_members_has_co':#31
                        jsonvar['group_ye18c77/group_yw8pj39/Does_any_family_members_has_co']=str(specialcharremover(str(value)))
                    elif key=="_xform_id_string":
                        jsonvar[key]=xform_id_string
                    elif key =="formhub/uuid":
                        jsonvar[key]=formhub_id
                    elif key =="__version__":
                        jsonvar[key]=versioncode
                    elif key== "meta/instanceID":
                        jsonvar[key]="uuid:"+str(uuid.uuid4())
                    elif key=="_userform_id":
                        jsonvar[key]=userform_id
                    elif key== "_id":
                        id_id = specialcharremover(str(value))
                    elif key == 'type_of_house_occupancy':#32
                        jsonvar['group_ce0hf58/Type_of_structure_occupancy']=str(specialcharremover(str(value)))
                    elif key == '_submitted_by':
                        jsonvar['_submitted_by']=value
                    elif key == 'end':
                        jsonvar['end']=value
                    elif key =='start':
                        jsonvar['start']=value
                    elif key =='_submission_time':
                        jsonvar['_submission_time']=value
                    else :
                        jsonvar['group_ye18c77/group_yw8pj39/where_the_individual_toilet_is_connected_to_']=str('08')
                        jsonvar['group_ye18c77/group_yw8pj39/what_is_the_status_of_toilet_under_sbm_  ']=str('04')
                        jsonvar['group_ye18c77/group_yw8pj39/type_of_toilet_preference'] = str('04')
                except Exception as ex:
                    print "hhhhhhhhhhhhh",ex
            xmldata=""
            xmldata = dict2xml({xform_id_string : jsonformat(jsonvar)})
            xmlfinal=""
            xmlfinal=str(xmldata.display()).replace('<'+xform_id_string+'>','<'+xform_id_string+'  id="'+xform_id_string+'" version="'+versioncode+'">').replace('<_xform_id_string/>','')
            filename=str("RHSFinal_"+city_id+"_"+admin_no+"_"+slum_no+"_"+house_no+"_"+ str(id_id)+".xml")
            with open(folder +"/"+filename, 'w') as f:
                f.write(xmlfinal)
                count = count + 1
                f.close()
    except Exception as ex:
        print ex


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
