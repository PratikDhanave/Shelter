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
import sys

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

listvar={}


house_no=""
admin_no=""
slum_no=""
city_id=""
id_id = ""

folder = "/home/softcorner/ShelterAssociates/src/scripts/RHS/xmlfiles/RapidHouseholdSurvey/"
sqlitepath="/storage/emulated/0/odk/instances/RHS Final_2016-12-09_11-00-10/"


def printdata():
    count = 0
    id_id = ""
    demo=0
    try:
        dataval=mongodb.instances.find({"_xform_id_string" :"abowbPoPd9YqKp6Z2VnZqb"})
        for data in dataval:
            listvar={}
            count = count + 1
            listvar['group_ce0hf58']= {}
            listvar['formhub'] = {}
            listvar['meta'] = {}
            listvar['group_ye18c77'] = {}
            listvar['group_ye18c77']['group_ud4em45'] = {}
            listvar['group_ye18c77']['group_yw8pj39'] = {}
            for key,value in data.items():
                try:
                    if key == 'group_ce0hf58/Selct_city':#1
                        listvar['group_ce0hf58'].update({'city':str("3789")})
                        city_id = str("3789")
                    elif key == 'group_ce0hf58/select_slum_of_admin_ward_c':#3
                        listvar['group_ce0hf58'].update({'slum_name':str(specialcharremover(str(value)))})
                        slum_no= str(specialcharremover(str(value)))
                    elif key == 'group_ce0hf58/select_slum_of_admin_e':#3
                        listvar['group_ce0hf58'].update({'slum_name':str(specialcharremover(str(value)))})
                        slum_no= str(specialcharremover(str(value)))
                    elif key == 'group_ce0hf58/select_slum_of_admin_f':#3
                        listvar['group_ce0hf58'].update({'slum_name':str(specialcharremover(str(value)))})
                        slum_no= str(specialcharremover(str(value)))
                    elif key == 'group_ce0hf58/Select_admin_ward':#2
                        if value == "03":
                            listvar['group_ce0hf58'].update({'admin_ward':str('PC03')})
                            admin_no = str("PC03")
                        elif value == "05":
                            listvar['group_ce0hf58'].update({'admin_ward':str('PC05')})
                            admin_no = str("PC05")
                        elif value == "06":
                            listvar['group_ce0hf58'].update({'admin_ward':str('PC06')})
                            admin_no = str("PC06")
                    elif key == 'group_ce0hf58/date_of_rhs':#4
                        listvar['group_ce0hf58'].update({'date_of_rhs':value})
                    elif key =='group_ce0hf58/name_of_surveyor_who_collected_rhs_data':#5
                        listvar['group_ce0hf58'].update({'name_of_surveyor_who_collected_rhs_data':str(specialcharremover(str(value)))})
                    elif key =='group_ce0hf58/house_no':#6
                        listvar['group_ce0hf58'].update({'house_no':str(specialcharremover(str(value)))})
                        house_no=str(specialcharremover(str(value)))
                    elif key == "group_ye18c77/group_yw8pj39/what_is_the_structure_of_the_house":#7
                        listvar['group_ye18c77']['group_yw8pj39']['what_is_the_structure_of_the_house']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_ud4em45/what_is_the_full_name_of_the_family_head_':#8
                        listvar['group_ye18c77']['group_ud4em45']['what_is_the_full_name_of_the_family_head_']={}
                        listvar['group_ye18c77']['group_ud4em45']['what_is_the_full_name_of_the_family_head_']=str(specialcharremover((value)))
                    elif key == 'group_ye18c77/group_ud4em45/mobile_number':#9
                        listvar['group_ye18c77']['group_ud4em45']['mobile_number']={}
                        listvar['group_ye18c77']['group_ud4em45']['mobile_number']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_ud4em45/adhar_card_number':#10
                        listvar['group_ye18c77']['group_ud4em45']['adhar_card_number']={}
                        listvar['group_ye18c77']['group_ud4em45']['adhar_card_number']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/what_is_the_ownership_status_of_the_house':#11
                        if value =='03':
                            print "**********value is 03*******" + value
                            listvar['group_ye18c77']['group_yw8pj39']['what_is_the_ownership_status_of_the_house']=str('01')
                        else:
                            listvar['group_ye18c77']['group_yw8pj39']['what_is_the_ownership_status_of_the_house']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/number_of_family_members':#12
                        listvar['group_ye18c77']['group_yw8pj39']['number_of_family_members']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/Do_you_have_a_girl_child_under':#13
                        listvar['group_ye18c77']['group_yw8pj39']['Do_you_have_a_girl_child_under']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/if_yes_how_many_':#14
                        listvar['group_ye18c77']['group_yw8pj39']['if_yes_how_many_']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/house_area_in_sq_ft':#15
                        listvar['group_ye18c77']['group_yw8pj39']['house_area_in_sq_ft']=str(specialcharremover(str(value)))
                    elif key =='group_ye18c77/group_yw8pj39/Current_place_of_defecation_t':#16
                        listvar['group_ye18c77']['group_yw8pj39']['Current_place_of_defecation_toilet'] = str(specialcharremover(str(value)))
                    elif key =='group_ye18c77/group_yw8pj39/where_the_individual_toilet_is_connected_to_':#17
                        listvar['group_ye18c77']['group_yw8pj39']['where_the_individual_toilet_is_connected_to_']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/type_of_water_connection':#18
                        listvar['group_ye18c77']['group_yw8pj39']['type_of_water_connection']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/facility_of_waste_collection':#19
                        if value == '01':
                            listvar['group_ye18c77']['group_yw8pj39']['facility_of_waste_collection']=str("01")
                        elif value == '02':
                            listvar['group_ye18c77']['group_yw8pj39']['facility_of_waste_collection']=str("03")
                        elif value =="03":
                            listvar['group_ye18c77']['group_yw8pj39']['facility_of_waste_collection']=str("02")
                        elif value == '04':
                            listvar['group_ye18c77']['group_yw8pj39']['facility_of_waste_collection']=str("03")
                        elif value == '05':
                            listvar['group_ye18c77']['group_yw8pj39']['facility_of_waste_collection']=str("03")
                        elif value =="06":
                            listvar['group_ye18c77']['group_yw8pj39']['facility_of_waste_collection']=str("04")
                        elif value == '07':
                            listvar['group_ye18c77']['group_yw8pj39']['facility_of_waste_collection']=str("06")
                        elif value =="08":
                            listvar['group_ye18c77']['group_yw8pj39']['facility_of_waste_collection']=str("07")
                        elif value =="09":
                            listvar['group_ye18c77']['group_yw8pj39']['facility_of_waste_collection']=str("05")
                        elif value =="10":
                            listvar['group_ye18c77']['group_yw8pj39']['facility_of_waste_collection']=str("01")
                    elif key == 'group_ye18c77/group_yw8pj39/Are_you_interested_in_individu':#20
                        listvar['group_ye18c77']['group_yw8pj39']['Are_you_interested_in_individu']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/if_yes_why_':#21
                        listvar['group_ye18c77']['group_yw8pj39']['if_yes_why_']=str(specialcharremover(str(value)))
                    elif key =='group_ye18c77/group_yw8pj39/if_no_why_':#22
                        listvar['group_ye18c77']['group_yw8pj39']['if_no_why_']=str(specialcharremover(str(value)))
                    elif key =='group_ye18c77/group_yw8pj39/type_of_toilet_preference':#23
                        listvar['group_ye18c77']['group_yw8pj39']['type_of_toilet_preference']=str(specialcharremover(str(value)))
                    elif key =='group_ye18c77/group_yw8pj39/Have_you_applied_for_indiviual':#24
                        listvar['group_ye18c77']['group_yw8pj39']['Have_you_applied_for_indiviual']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/How_many_installements_have_yo':#25
                        listvar['group_ye18c77']['group_yw8pj39']['How_many_installements_have_yo']=value
                    elif key == 'group_ye18c77/group_yw8pj39/does_any_member_of_your_family_go_for_open_defecation_':#26
                        listvar['group_ye18c77']['group_yw8pj39']['does_any_member_of_your_family_go_for_open_defecation_']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/when_did_you_receive_the_first_installment_date':#28
                        listvar['group_ye18c77']['group_yw8pj39']['when_did_you_receive_the_first_installment_date']=value
                    elif key == 'group_ye18c77/group_yw8pj39/when_did_you_receive_the_second_installment_date':#29
                        listvar['group_ye18c77']['group_yw8pj39']['when_did_you_receive_the_second_installment_date']=value
                    elif key == 'group_ye18c77/group_yw8pj39/what_is_the_status_of_toilet_under_sbm':#30
                        listvar['group_ye18c77']['group_yw8pj39']['what_is_thehave_status_of_toilet_under_sbm_']=str(specialcharremover(str(value)))
                    elif key == 'group_ye18c77/group_yw8pj39/Does_any_family_members_has_co':#31
                        listvar['group_ye18c77']['group_yw8pj39']['Does_any_family_members_has_co']=str(specialcharremover(str(value)))
                    elif key=="_xform_id_string":
                        listvar['_xform_id_string']= {}
                        listvar['_xform_id_string']=str(xform_id_string)
                    elif key =="formhub/uuid":
                        listvar['formhub']['uuid']= {}
                        listvar['formhub']['uuid']=formhub_id
                    elif key =="__version__":
                        listvar['__version__']={}
                        listvar['__version__']=versioncode
                    elif key== "meta/instanceID":
                        listvar['meta']['instanceID']= {}
                        listvar['meta']['instanceID']= "uuid:" + str(uuid.uuid4())
                    elif key=="_userform_id":
                        listvar['_userform_id']={}
                        listvar['_userform_id']=userform_id
                    elif key== "_id":
                        id_id = specialcharremover(str(value))
                    elif key == 'Type_of_structure_occupancy':#32
                        listvar['group_ce0hf58'].update({'Type_of_structure_occupancy':str(specialcharremover(str(value)))})
                    elif key == '_submitted_by':
                        listvar['_submitted_by']={}
                        listvar['_submitted_by']=value
                    elif key == 'end':
                        listvar['end']={}
                        listvar['end']=value
                    elif key =='start':
                        listvar['start']={}
                        listvar['start']=value
                    elif key =='_submission_time':
                        listvar['_submission_time']={}
                        listvar['_submission_time']=value
                except Exception as ex:
                    print "hhhhhhhhhhhhh",ex
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



def func(keyls):
	list_data=[]
	print keyls.keys()[0],keyls.values()[0]
	dbslum(keyls.keys()[0],keyls.values()[0])
	extraTypeSlum(keyls.keys()[0],keyls.values()[0])




def main():
    printdata()


if __name__ == '__main__':
    main()
