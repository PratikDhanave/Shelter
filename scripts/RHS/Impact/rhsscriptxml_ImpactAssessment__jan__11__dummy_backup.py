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

jsonvar  = {}

xform_id_string="aG8SrJfKazUbY5TtpyKTu8"
versioncode="vRU8dbywUfTBWmFUejPmSt"
formhub_id="fce6bc09f36047049919e912a6e05722"
userform_id="softcorner_aG8SrJfKazUbY5TtpyKTu8"

client = MongoClient('mongodb://127.0.0.1:27017/')

#databse name
mongodb = client['shelterlive']

listvar={}

house_no=""
admin_no=""
slum_no=""
city_id=""
id_id = ""

folder = "/home/softcorner/ShelterAssociates/src/scripts/RHS/xmlfiles/Impact"
sqlitepath="/storage/emulated/0/odk/instances/RHS Final_2016-12-09_11-00-10/"


def printdata():
    count = 0
    id_id = ""
    demo=0
    try:
        dataval=mongodb.instances.find({"_xform_id_string" :"aSJM5YWy8LXcmHYL3ZMGgY","group_fz8ww97/Phone_Number": "8888321174"})
        for data in dataval:
            count = count + 1
            listvar['group_eh0at37']= {}
            listvar['group_qc6ug62']= {}
            listvar['group_fz8ww97']= {}
            listvar['group_wd4ew27'] = {}
            listvar['group_tx1ao07'] = {}
            listvar['group_cl1xw20'] = {}
            listvar['group_dg2zj23'] = {}
            listvar['formhub'] = {}
            listvar['meta'] = {}
            listvar['group_wd4ew27']['group_tc8ri87'] = {}
            listvar['group_wd4ew27']['group_pa3cb33'] = {}
            listvar['group_wd4ew27']['group_ki1ef63'] = {}
            for key,value in data.items():
                if key == 'group_eh0at37/In_case_of_shared_toilets_how':
                    listvar['group_eh0at37'].update({'In_case_of_shared_toilets_how':value})
                elif key == 'group_eh0at37/Is_CTB_open_throughout_the_day':#94
                    listvar['group_eh0at37'].update({'Is_CTB_open_throughout_the_day':value})
                elif key == 'group_eh0at37/When_is_the_CTB_closed_during_':#95
                    listvar['group_eh0at37'].update({'When_is_the_CTB_closed_during_':value})
                elif key == 'group_eh0at37/Is_CTB_open_throughout_the_nig':#96
                    listvar['group_eh0at37'].update({'Is_CTB_open_throughout_the_nig':value})
                elif key == 'group_eh0at37/When_is_the_CTB_closed_during__001':#97
                    listvar['group_eh0at37'].update({'When_is_the_CTB_closed_during__001':value})
                elif key == 'group_eh0at37/Do_you_pay_fees_for_the_use_of':#98
                    listvar['group_eh0at37'].update({'Do_you_pay_fees_for_the_use_of':value})
                elif key == 'group_eh0at37/Do_you_pay_the_amount_per_visi':#99
                    listvar['group_eh0at37'].update({'Do_you_pay_the_amount_per_visi':value})
                elif key == 'group_eh0at37/What_is_the_amount_Urination':#100
                    listvar['group_eh0at37'].update({'What_is_the_amount_Urination':value})
                elif key == 'group_eh0at37/What_is_the_amount_Toilet':#101
                    listvar['group_eh0at37'].update({'What_is_the_amount_Toilet':value})
                elif key == 'group_eh0at37/What_is_the_amount_Bathing':#102
                    listvar['group_eh0at37'].update({'What_is_the_amount_Bathing':value})
                elif key == 'group_eh0at37/What_is_the_amount_Flat_per_m':#103
                    listvar['group_eh0at37'].update({'What_is_the_amount_Flat_per_m':value})
                elif key == 'group_eh0at37/_Observe_and_write_Do_you_see':#104
                    listvar['group_eh0at37'].update({'_Observe_and_write_Do_you_see':value})
                elif key == 'group_eh0at37/Whether_the_household_faced_pr':#105
                    listvar['group_eh0at37'].update({'Whether_the_household_faced_pr':value})
                elif key == 'group_eh0at37/group_oq8lx49':
                    finalarray = []
                    for i in value:
                        arraydict = {}
                        for ke,val in i.items():
                            if ke == 'group_eh0at37/group_oq8lx49/Name_of_the_family_member_001':#82#
                                arraydict['Name_of_the_family_member_001']=str(specialcharremover(str(val)))
                            elif ke == 'group_eh0at37/group_oq8lx49/where_is_the_place_of_urinatio':#83
                                arraydict['where_is_the_place_of_urinatio']=str(specialcharremover(str(val)))
                            elif ke == 'group_eh0at37/group_oq8lx49/Other_place_of_urination':#84
                                arraydict['Other_place_of_urination']=str(specialcharremover(str(val)))
                            elif ke == 'group_eh0at37/group_oq8lx49/where_is_the_place_of_urinatio_001':#85
                                arraydict['where_is_the_place_of_urinatio_001']=str(specialcharremover(str(val)))
                            elif ke == 'group_eh0at37/group_oq8lx49/Other_place_of_defecation':#85
                                arraydict['Other_place_of_defecation']=str(specialcharremover(str(val)))
                            elif ke == 'group_eh0at37/group_oq8lx49/What_is_the_reason_of_choosing':#86
                                arraydict['What_is_the_reason_of_choosing']=str(specialcharremover(str(val)))
                            elif ke == 'group_eh0at37/group_oq8lx49/Other_reason_for_choosing_curr':#87
                                arraydict['Other_reason_for_choosing_curr']=str(specialcharremover(str(val)))
                            elif ke == 'group_eh0at37/group_oq8lx49/What_are_the_problems_associat':#88
                                arraydict['What_are_the_problems_associat']=str(specialcharremover(str(val)))
                            elif ke == 'group_eh0at37/group_oq8lx49/Other_Problem_associated_with_':#89
                                arraydict['Other_Problem_associated_with_']=str(specialcharremover(str(val)))
                            elif ke == 'group_eh0at37/group_oq8lx49/If_children_elderly_defecating':#90
                                arraydict['If_children_elderly_defecating']=str(specialcharremover(str(val)))
                            elif ke == 'group_eh0at37/group_oq8lx49/What_are_the_problems_associat_001':#91
                                arraydict['What_are_the_problems_associat_001']=str(specialcharremover(str(val)))
                            elif ke == 'group_eh0at37/group_oq8lx49/Other_problems_associated_with':#92
                                arraydict['Other_problems_associated_with']=str(specialcharremover(str(val)))
                        finalarray.append(arraydict)
                        listvar['group_eh0at37']['group_oq8lx49']={}
                        listvar['group_eh0at37']['group_oq8lx49']=finalarray
                elif key == 'group_nw4qu40':
                    finalarray = []
                    for i in value:
                        arraydict = {}
                        for ke,val in i.items():
                            if ke =='group_nw4qu40/Sex':#10
                                arraydict['Sex']=str(specialcharremover(str(val)))
                            elif ke == 'group_nw4qu40/Marital_Status':#11
                                arraydict['Marital_Status']=str(specialcharremover(str(val)))
                            elif ke == 'group_nw4qu40/Education':#12
                                arraydict['Education']=str(specialcharremover(str(val)))
                            elif ke == 'group_nw4qu40/Occupation':#13
                                arraydict['Occupation']=str(specialcharremover(str(val)))
                            elif ke == 'group_nw4qu40/Special_Characteristics':#14
                                arraydict['Special_Characteristics']=str(specialcharremover(str(val)))
                            elif ke == 'group_nw4qu40/Name_of_the_family_Member':#8
                                arraydict['Name_of_the_family_Member']=str(specialcharremover(str(val)))
                            elif ke == 'group_nw4qu40/Completed_Age_in_years':#9
                                arraydict['Completed_Age_in_years']=str(val)
                        finalarray.append(arraydict)
                        print finalarray
                        listvar['group_nw4qu40'] = {}
                        listvar['group_nw4qu40']=finalarray
                elif key == 'group_mw2gr61':
                    finalarray = []
                    for i in value:
                        arraydict = {}
                        for ke,val in i.items():
                            if ke == 'group_mw2gr61/Name_of_family_member':#119
                                arraydict['Name_of_family_member']=str(specialcharremover(str(val)))
                            elif ke == 'group_mw2gr61/Did_Name_suffer_from_any_o':#120
                                arraydict['Did_Name_suffer_from_any_o']=str(specialcharremover(str(val)))
                            elif ke == 'group_mw2gr61/Other_illness':#121
                                arraydict['Other_illness']=str(specialcharremover(str(val)))
                            elif ke == 'group_mw2gr61/Has_Name_sought_treatment_fo':#122
                                arraydict['Has_Name_sought_treatment_fo']=str(specialcharremover(str(val)))
                            elif ke == 'group_mw2gr61/What_are_the_expenses_for_the_':#123
                                arraydict['What_are_the_expenses_for_the_']=str(specialcharremover(str(val)))
                        finalarray.append(arraydict)
                        listvar['group_mw2gr61'] = {}
                        listvar['group_mw2gr61']=finalarray
                elif key == 'group_mw6ct68':
                    finalarray = []
                    for i in value:
                        arraydict = {}
                        for ke,val in i.items():
                            if ke == 'group_mw6ct68/Name_of_Family_member_002':#124
                                arraydict['Name_of_Family_member_002']=str(specialcharremover(str(val)))
                            elif ke == 'group_mw6ct68/Did_you_suffer_from_any_of_the':#125
                                arraydict['Did_you_suffer_from_any_of_the']=str(specialcharremover(str(val)))
                            elif ke == 'group_mw6ct68/Did_you_suffer_from_any_of_the_001':#126
                                arraydict['Did_you_suffer_from_any_of_the_001']=str(specialcharremover(str(val)))
                            elif ke == 'group_mw6ct68/Did_you_suffer_from_any_of_the_002':#127
                                arraydict['Did_you_suffer_from_any_of_the_002']=str(specialcharremover(str(val)))
                            elif ke == 'group_mw6ct68/Do_you_think_extra_cleanliness':#128
                                arraydict['Do_you_think_extra_cleanliness']=str(specialcharremover(str(val)))
                            elif ke == 'group_mw6ct68/During_menstrual_period_how_m':#129
                                arraydict['During_menstrual_period_how_m']=str(specialcharremover(str(val)))
                            elif ke == 'group_mw6ct68/How_often_have_you_washed_your':#130
                                arraydict['How_often_have_you_washed_your']=str(specialcharremover(str(val)))
                        finalarray.append(arraydict)
                        listvar['group_mw6ct68'] = {}
                        listvar['group_mw6ct68']=finalarray
                elif key == 'group_qc6ug62/group_om1sb12':
                    finalarray = []
                    for i in value:
                        arraydict = {}
                        for ke,val in i.items():
                            if ke == 'group_qc6ug62/group_om1sb12/Name_of_family_member_001':#136
                                arraydict['Name_of_family_member_001']=str(specialcharremover(str(val)))
                            elif ke == 'group_qc6ug62/group_om1sb12/Teasing':#137
                                arraydict['Teasing']=str(specialcharremover(str(val)))
                            elif ke == 'group_qc6ug62/group_om1sb12/Physical_abuse':#138
                                arraydict['Physical_abuse']=str(specialcharremover(str(val)))
                            elif ke == 'group_qc6ug62/group_om1sb12/Animal_bite':#139
                                arraydict['Animal_bite']=str(specialcharremover(str(val)))
                            elif ke == 'group_qc6ug62/group_om1sb12/Insect_bite':#140
                                arraydict['Insect_bite']=str(specialcharremover(str(val)))
                            elif ke == 'group_qc6ug62/group_om1sb12/How_safe_do_you_feel_while_usi':#141
                                arraydict['How_safe_do_you_feel_while_usi']=str(specialcharremover(str(val)))
                            elif ke == 'group_qc6ug62/group_om1sb12/How_safe_do_you_feel_while_def':#142
                                arraydict['How_safe_do_you_feel_while_def']=str(specialcharremover(str(val)))
                            elif ke == 'group_qc6ug62/group_om1sb12/How_safe_do_you_feel_while_app':#143
                                arraydict['How_safe_do_you_feel_while_app']=str(specialcharremover(str(val)))
                            elif ke == 'group_qc6ug62/group_om1sb12/How_would_you_rate_the_privacy':#144
                                arraydict['How_would_you_rate_the_privacy']=str(specialcharremover(str(val)))
                            elif ke == 'group_qc6ug62/group_om1sb12/How_would_you_rate_the_privacy_001':#145
                                arraydict['How_would_you_rate_the_privacy_001']=str(specialcharremover(str(val)))
                            elif ke == 'group_qc6ug62/group_om1sb12/How_would_you_rate_the_distanc':#146
                                arraydict['How_would_you_rate_the_distanc']=str(specialcharremover(str(val)))
                        finalarray.append(arraydict)
                        listvar['group_qc6ug62']['group_om1sb12']={}
                        listvar['group_qc6ug62']['group_om1sb12']=finalarray
                elif key == 'group_fz8ww97/Name_of_City':#1
                    listvar['group_fz8ww97']['Name_of_City']={}
                    listvar['group_fz8ww97']['Name_of_City']=str(specialcharremover(str(value)))
                elif key == 'group_fz8ww97/Name_of_Slum':#2
                    listvar['group_fz8ww97']['Name_of_Slum']={}
                    listvar['group_fz8ww97']['Name_of_Slum']=str(specialcharremover(str(value)))
                    slum_no = str(specialcharremover(str(value)))
                elif key == 'group_fz8ww97/Household_Number':#3
                    listvar['group_fz8ww97']['Household_Number']={}
                    listvar['group_fz8ww97']['Household_Number']=str(specialcharremover(str(value)))
                    house_no=str(specialcharremover(str(value)))
                elif key == 'group_fz8ww97/Name_of_Interviewer':#4
                    listvar['group_fz8ww97']['Name_of_Interviewer']={}
                    listvar['group_fz8ww97']['Name_of_Interviewer']=str(specialcharremover(str(value)))
                elif key =='group_fz8ww97/Date_of_Interview':#5
                    listvar['group_fz8ww97']['Date_of_Interview']={}
                    listvar['group_fz8ww97']['Date_of_Interview']=value
                elif key =='group_fz8ww97/Name_of_Respondent':#6
                    listvar['group_fz8ww97']['Name_of_Respondent']={}
                    listvar['group_fz8ww97']['Name_of_Respondent']=str(specialcharremover(str(value)))
                elif key == "group_fz8ww97/Phone_Number":#7
                    listvar['group_fz8ww97']['Phone_Number']={}
                    listvar['group_fz8ww97']['Phone_Number']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/Type_of_family':#15
                    listvar['group_wd4ew27']['Type_of_family']={}
                    listvar['group_wd4ew27']['Type_of_family']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/Religion_of_the_family':#16
                    listvar['group_wd4ew27']['Religion_of_the_family']={}
                    listvar['group_wd4ew27']['Religion_of_the_family']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/What_is_the_caste_of_the_head_':#17
                    listvar['group_wd4ew27']['What_is_the_caste_of_the_head_']={}
                    listvar['group_wd4ew27']['What_is_the_caste_of_the_head_']=str(specialcharremover(str(value)))
                elif key =='group_wd4ew27/What_is_the_caste_or_tribe_of_':#18
                    listvar['group_wd4ew27']['What_is_the_caste_or_tribe_of_']={}
                    listvar['group_wd4ew27']['What_is_the_caste_or_tribe_of_']=str(specialcharremover(str(value)))
                elif key =='group_wd4ew27/How_is_the_approach_road_to_th':#19
                    listvar['group_wd4ew27']['How_is_the_approach_road_to_th']={}
                    listvar['group_wd4ew27']['How_is_the_approach_road_to_th']=str(specialcharremover(str(value)))
                elif key =='group_wd4ew27/_Observe_and_write_What_is_th':#20
                    listvar['group_wd4ew27']['_Observe_and_write_What_is_th']={}
                    listvar['group_wd4ew27']['_Observe_and_write_What_is_th']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/How_many_years_are_you_staying':#21
                    listvar['group_wd4ew27']['How_many_years_are_you_staying']={}
                    listvar['group_wd4ew27']['How_many_years_are_you_staying']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/What_is_the_ownership_status_o':#22
                    listvar['group_wd4ew27']['What_is_the_ownership_status_o']={}
                    listvar['group_wd4ew27']['What_is_the_ownership_status_o']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/Does_any_member_of_this_househ':#23
                    listvar['group_wd4ew27']['Does_any_member_of_this_househ']={}
                    listvar['group_wd4ew27']['Does_any_member_of_this_househ']=str(specialcharremover(str(value)))
                elif key =='group_wd4ew27/Does_any_member_of_this_househ_001':#24
                    listvar['group_wd4ew27']['Does_any_member_of_this_househ_001']={}
                    listvar['group_wd4ew27']['Does_any_member_of_this_househ_001']=str(specialcharremover(str(value)))
                elif key =='group_wd4ew27/How_many_floors_does_the_house':#25
                    listvar['group_wd4ew27']['How_many_floors_does_the_house']={}
                    listvar['group_wd4ew27']['How_many_floors_does_the_house']=str(specialcharremover(str(value)))
                elif key =='group_wd4ew27/How_many_rooms_does_the_house_':#26
                    listvar['group_wd4ew27']['How_many_rooms_does_the_house_']={}
                    listvar['group_wd4ew27']['How_many_rooms_does_the_house_']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/When_was_the_house_built':#27
                    listvar['group_wd4ew27']['When_was_the_house_built']={}
                    listvar['group_wd4ew27']['When_was_the_house_built']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_tc8ri87/Material_used_for_floor_Obser':#28
                    listvar['group_wd4ew27']['group_tc8ri87']['Material_used_for_floor_Obser']={}
                    listvar['group_wd4ew27']['group_tc8ri87']['Material_used_for_floor_Obser']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_tc8ri87/Material_used_for_walls_Obser':#29
                    listvar['group_wd4ew27']['group_tc8ri87']['Material_used_for_walls_Obser']={}
                    listvar['group_wd4ew27']['group_tc8ri87']['Material_used_for_walls_Obser']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_tc8ri87/Material_used_for_roof_Observ':#30
                    listvar['group_wd4ew27']['group_tc8ri87']['Material_used_for_roof_Observ']={}
                    listvar['group_wd4ew27']['group_tc8ri87']['Material_used_for_roof_Observ']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_tc8ri87/What_is_the_type_of_constructi':#31
                    listvar['group_wd4ew27']['group_tc8ri87']['What_is_the_type_of_constructi']={}
                    listvar['group_wd4ew27']['group_tc8ri87']['What_is_the_type_of_constructi']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/What_is_the_approximate_area_o':#32
                    listvar['group_wd4ew27']['What_is_the_approximate_area_o']={}
                    listvar['group_wd4ew27']['What_is_the_approximate_area_o']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/Does_the_house_have_electricit':#33
                    listvar['group_wd4ew27']['Does_the_house_have_electricit']={}
                    listvar['group_wd4ew27']['Does_the_house_have_electricit']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/How_many_windows_does_the_hous':#34
                    listvar['group_wd4ew27']['How_many_windows_does_the_hous']={}
                    listvar['group_wd4ew27']['How_many_windows_does_the_hous']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/Is_there_sufficient_sunlight_i':#35
                    listvar['group_wd4ew27']['Is_there_sufficient_sunlight_i']={}
                    listvar['group_wd4ew27']['Is_there_sufficient_sunlight_i']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/Is_there_adequate_ventilation_':#36
                    listvar['group_wd4ew27']['Is_there_adequate_ventilation_']={}
                    listvar['group_wd4ew27']['Is_there_adequate_ventilation_']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/Does_the_head_of_household_pos':#37
                    listvar['group_wd4ew27']['Does_the_head_of_household_pos']={}
                    listvar['group_wd4ew27']['Does_the_head_of_household_pos']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/Does_any_usual_resident_of_thi':#38
                    listvar['group_wd4ew27']['Does_any_usual_resident_of_thi']={}
                    listvar['group_wd4ew27']['Does_any_usual_resident_of_thi']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/What_is_the_main_fuel_does_the':#39
                    listvar['group_wd4ew27']['What_is_the_main_fuel_does_the']={}
                    listvar['group_wd4ew27']['What_is_the_main_fuel_does_the']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_pa3cb33/Does_your_house_have_A_mattre':#40
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_mattre']={}
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_mattre']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_pa3cb33/Does_your_house_have_A_pressu':#41
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_pressu']={}
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_pressu']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_pa3cb33/Does_your_house_have_A_chair':#42
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_chair']={}
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_chair']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_pa3cb33/Does_your_house_have_A_table':#43
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_table']={}
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_table']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_pa3cb33/Does_your_house_have_A_cot_or':#44
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_cot_or']={}
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_cot_or']=str(specialcharremover(str(value)))
                elif key =='group_wd4ew27/group_pa3cb33/Does_your_house_have_An_elect':#45
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_An_elect']={}
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_An_elect']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_pa3cb33/Does_your_house_have_A_black_':#46
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_black_']={}
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_black_']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_pa3cb33/Does_your_house_have_A_colour':#47
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_colour']={}
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_colour']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_pa3cb33/Does_your_house_have_A_Cable_':#48
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_Cable_']={}
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_Cable_']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_pa3cb33/Does_your_house_have_A_sewing':#49
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_sewing']={}
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_sewing']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_pa3cb33/Does_your_house_have_A_mobile':#50
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_mobile']={}
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_mobile']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_pa3cb33/Does_your_house_have_A_radio_':#51
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_radio_']={}
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_radio_']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_pa3cb33/Does_your_house_have_A_landli':#52
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_landli']={}
                    listvar['group_wd4ew27']['group_pa3cb33']['Does_your_house_have_A_landli']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_ki1ef63/Does_your_house_have_Internet':#53
                    listvar['group_wd4ew27']['group_ki1ef63']['Does_your_house_have_Internet']={}
                    listvar['group_wd4ew27']['group_ki1ef63']['Does_your_house_have_Internet']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_ki1ef63/Does_your_house_have_A_comput':#54
                    listvar['group_wd4ew27']['group_ki1ef63']['Does_your_house_have_A_comput']={}
                    listvar['group_wd4ew27']['group_ki1ef63']['Does_your_house_have_A_comput']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_ki1ef63/Does_your_house_have_A_refrig':#62
                    listvar['group_wd4ew27']['group_ki1ef63']['Does_your_house_have_A_refrig']={}
                    listvar['group_wd4ew27']['group_ki1ef63']['Does_your_house_have_A_refrig']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_ki1ef63/Does_your_house_have_A_washin':#55
                    listvar['group_wd4ew27']['group_ki1ef63']['Does_your_house_have_A_washin']={}
                    listvar['group_wd4ew27']['group_ki1ef63']['Does_your_house_have_A_washin']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_ki1ef63/Does_your_house_have_A_watch_':#56
                    listvar['group_wd4ew27']['group_ki1ef63']['Does_your_house_have_A_watch_']={}
                    listvar['group_wd4ew27']['group_ki1ef63']['Does_your_house_have_A_watch_']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_ki1ef63/Does_your_house_have_A_bicycl':#57
                    listvar['group_wd4ew27']['group_ki1ef63']['Does_your_house_have_A_bicycl']={}
                    listvar['group_wd4ew27']['group_ki1ef63']['Does_your_house_have_A_bicycl']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_ki1ef63/Does_your_house_have_A_cooler':#58
                    listvar['group_wd4ew27']['group_ki1ef63']['Does_your_house_have_A_cooler']={}
                    listvar['group_wd4ew27']['group_ki1ef63']['Does_your_house_have_A_cooler']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_ki1ef63/Does_your_house_have_A_Ricksh':#59
                    listvar['group_wd4ew27']['group_ki1ef63']['Does_your_house_have_A_Ricksh']={}
                    listvar['group_wd4ew27']['group_ki1ef63']['Does_your_house_have_A_Ricksh']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_ki1ef63/Does_your_house_have_A_motorc':#60
                    listvar['group_wd4ew27']['group_ki1ef63']['Does_your_house_have_A_motorc']={}
                    listvar['group_wd4ew27']['group_ki1ef63']['Does_your_house_have_A_motorc']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/group_ki1ef63/Does_your_house_have_A_Pushca':#61
                    listvar['group_wd4ew27']['group_ki1ef63']['Does_your_house_have_A_Pushca']={}
                    listvar['group_wd4ew27']['group_ki1ef63']['Does_your_house_have_A_Pushca']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/What_is_the_main_source_of_wat':#62
                    listvar['group_wd4ew27']['What_is_the_main_source_of_wat']={}
                    listvar['group_wd4ew27']['What_is_the_main_source_of_wat']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/Other_Source_of_water':##63
                    listvar['group_wd4ew27']['Other_Source_of_water']={}
                    listvar['group_wd4ew27']['Other_Source_of_water']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/What_is_the_normal_frequency_o':##64
                    listvar['group_wd4ew27']['What_is_the_normal_frequency_o']={}
                    listvar['group_wd4ew27']['What_is_the_normal_frequency_o']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/What_is_the_current_frequency_':#65
                    listvar['group_wd4ew27']['What_is_the_current_frequency_']={}
                    listvar['group_wd4ew27']['What_is_the_current_frequency_']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/Do_you_get_sufficient_water_th':#66
                    listvar['group_wd4ew27']['Do_you_get_sufficient_water_th']={}
                    listvar['group_wd4ew27']['Do_you_get_sufficient_water_th']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/How_many_months_in_a_year_do_y':#67
                    listvar['group_wd4ew27']['How_many_months_in_a_year_do_y']={}
                    listvar['group_wd4ew27']['How_many_months_in_a_year_do_y']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/What_are_the_other_alternative':#68
                    listvar['group_wd4ew27']['What_are_the_other_alternative']={}
                    listvar['group_wd4ew27']['What_are_the_other_alternative']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/Other_alternative_source_of_wa':#69
                    listvar['group_wd4ew27']['Other_alternative_source_of_wa']={}
                    listvar['group_wd4ew27']['Other_alternative_source_of_wa']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/Who_fetches_the_water_if_the_s':#70
                    listvar['group_wd4ew27']['Other_alternative_source_of_wa']={}
                    listvar['group_wd4ew27']['Other_alternative_source_of_wa']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/How_much_time_does_it_take_to_':#71
                    listvar['group_wd4ew27']['How_much_time_does_it_take_to_']={}
                    listvar['group_wd4ew27']['How_much_time_does_it_take_to_']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/Do_you_have_access_to_a_bathro':#72
                    listvar['group_wd4ew27']['Do_you_have_access_to_a_bathro']={}
                    listvar['group_wd4ew27']['Do_you_have_access_to_a_bathro']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/Access_to_bathroom_Other':#73
                    listvar['group_wd4ew27']['Access_to_bathroom_Other']={}
                    listvar['group_wd4ew27']['Access_to_bathroom_Other']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/What_is_the_area_of_bathroom':#74
                    listvar['group_wd4ew27']['What_is_the_area_of_bathroom']={}
                    listvar['group_wd4ew27']['What_is_the_area_of_bathroom']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/Does_this_house_have_access_to':#75
                    listvar['group_wd4ew27']['Does_this_house_have_access_to']={}
                    listvar['group_wd4ew27']['Does_this_house_have_access_to']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/What_are_the_issues_associated':#76
                    listvar['group_wd4ew27']['What_are_the_issues_associated']={}
                    listvar['group_wd4ew27']['What_are_the_issues_associated']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/Other_issues_related_to_draina':#77
                    listvar['group_wd4ew27']['Other_issues_related_to_draina']={}
                    listvar['group_wd4ew27']['Other_issues_related_to_draina']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/How_many_times_do_you_need_to_':#78
                    listvar['group_wd4ew27']['How_many_times_do_you_need_to_']={}
                    listvar['group_wd4ew27']['How_many_times_do_you_need_to_']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/Do_you_visit_or_avoid_visiting_001':#79
                    listvar['group_wd4ew27']['Do_you_visit_or_avoid_visiting_001']={}
                    listvar['group_wd4ew27']['Do_you_visit_or_avoid_visiting_001']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/How_many_times_do_you_need_to_001':#80
                    listvar['group_wd4ew27']['How_many_times_do_you_need_to_001']={}
                    listvar['group_wd4ew27']['How_many_times_do_you_need_to_001']=str(specialcharremover(str(value)))
                elif key == 'group_wd4ew27/Do_you_visit_or_avoid_visiting':#81
                    listvar['group_wd4ew27']['Do_you_visit_or_avoid_visiting']={}
                    listvar['group_wd4ew27']['Do_you_visit_or_avoid_visiting']=str(specialcharremover(str(value)))
                elif key == 'group_tx1ao07/Are_you_aware_about_toilet_cle':#106
                    listvar['group_tx1ao07']['Are_you_aware_about_toilet_cle']={}
                    listvar['group_tx1ao07']['Are_you_aware_about_toilet_cle']=str(specialcharremover(str(value)))
                elif key == 'group_tx1ao07/How_often_should_toilets_be_cl':#107
                    listvar['group_tx1ao07']['How_often_should_toilets_be_cl']={}
                    listvar['group_tx1ao07']['How_often_should_toilets_be_cl']=str(specialcharremover(str(value)))
                elif key == 'group_tx1ao07/What_material_would_you_use_to':#108
                    listvar['group_tx1ao07']['What_material_would_you_use_to']={}
                    listvar['group_tx1ao07']['What_material_would_you_use_to']=str(specialcharremover(str(value)))
                elif key == 'group_tx1ao07/Have_you_heard_about_Swatch_Bh':#109
                    listvar['group_tx1ao07']['Have_you_heard_about_Swatch_Bh']={}
                    listvar['group_tx1ao07']['Have_you_heard_about_Swatch_Bh']=str(specialcharremover(str(value)))
                elif key == 'group_tx1ao07/What_do_you_know_about_Swatch_':#110
                    listvar['group_tx1ao07']['What_do_you_know_about_Swatch_']={}
                    listvar['group_tx1ao07']['What_do_you_know_about_Swatch_']=str(specialcharremover(str(value)))
                elif key == 'group_tx1ao07/Do_you_treat_drinking_water':#111
                    listvar['group_tx1ao07']['Do_you_treat_drinking_water']={}
                    listvar['group_tx1ao07']['Do_you_treat_drinking_water']=str(specialcharremover(str(value)))
                elif key == 'group_tx1ao07/How_do_you_treat_the_drinking_':#112
                    listvar['group_tx1ao07']['How_do_you_treat_the_drinking_']={}
                    listvar['group_tx1ao07']['How_do_you_treat_the_drinking_']=str(specialcharremover(str(value)))
                elif key == 'group_tx1ao07/_Observe_and_write_Please_sho':#113
                    listvar['group_tx1ao07']['_Observe_and_write_Please_sho']={}
                    listvar['group_tx1ao07']['_Observe_and_write_Please_sho']=str(specialcharremover(str(value)))
                elif key == 'group_tx1ao07/With_what_do_you_wash_your_ha':#114
                    listvar['group_tx1ao07']['With_what_do_you_wash_your_ha']={}
                    listvar['group_tx1ao07']['With_what_do_you_wash_your_ha']=str(specialcharremover(str(value)))
                elif key == 'group_tx1ao07/In_the_past_7_days_how_many_t':#115
                    listvar['group_tx1ao07']['In_the_past_7_days_how_many_t']={}
                    listvar['group_tx1ao07']['In_the_past_7_days_how_many_t']=str(specialcharremover(str(value)))
                elif key == 'group_cl1xw20/Do_you_follow_any_restrictions':#116
                    listvar['group_cl1xw20']['Do_you_follow_any_restrictions']={}
                    listvar['group_cl1xw20']['Do_you_follow_any_restrictions']=str(specialcharremover(str(value)))
                elif key == 'group_cl1xw20/Do_you_avoid_drinking_water_':#117
                    listvar['group_cl1xw20']['Do_you_avoid_drinking_water_']={}
                    listvar['group_cl1xw20']['Do_you_avoid_drinking_water_']=str(specialcharremover(str(value)))
                elif key == 'group_cl1xw20/If_lesser_consumption_of_liqui':#118
                    listvar['group_cl1xw20']['If_lesser_consumption_of_liqui']={}
                    listvar['group_cl1xw20']['If_lesser_consumption_of_liqui']=str(specialcharremover(str(value)))
                elif key == 'group_qc6ug62/Are_community_toilets_safe_for':#131
                    listvar['group_qc6ug62']['Are_community_toilets_safe_for']={}
                    listvar['group_qc6ug62']['Are_community_toilets_safe_for']=str(specialcharremover(str(value)))
                elif key == 'group_qc6ug62/Do_women_girls_need_to_be_acco':#132
                    listvar['group_qc6ug62']['Do_women_girls_need_to_be_acco']={}
                    listvar['group_qc6ug62']['Do_women_girls_need_to_be_acco']=str(specialcharremover(str(value)))
                elif key == 'group_qc6ug62/Do_women_girls_need_to_be_acco_001':#133
                    listvar['group_qc6ug62']['Do_women_girls_need_to_be_acco_001']={}
                    listvar['group_qc6ug62']['Do_women_girls_need_to_be_acco_001']=str(specialcharremover(str(value)))
                elif key == 'group_qc6ug62/What_are_the_problems_that_wom':#134
                    listvar['group_qc6ug62']['What_are_the_problems_that_wom']={}
                    listvar['group_qc6ug62']['What_are_the_problems_that_wom']=str(specialcharremover(str(value)))
                elif key == 'group_qc6ug62/Other_problems_that_women_face':#135
                    listvar['group_qc6ug62']['Other_problems_that_women_face']={}
                    listvar['group_qc6ug62']['Other_problems_that_women_face']=str(specialcharremover(str(value)))
                elif key == 'group_dg2zj23/How_many_houses_in_your_neighb':#147
                    listvar['group_dg2zj23']['How_many_houses_in_your_neighb']={}
                    listvar['group_dg2zj23']['How_many_houses_in_your_neighb']=str(specialcharremover(str(value)))
                elif key == 'group_dg2zj23/What_are_the_advantages_of_hav':#148
                    listvar['group_dg2zj23']['What_are_the_advantages_of_hav']={}
                    listvar['group_dg2zj23']['What_are_the_advantages_of_hav']=str(specialcharremover(str(value)))
                elif key == 'group_dg2zj23/Other_Advatage_of_having_own_t':#149
                    listvar['group_dg2zj23']['Other_Advatage_of_having_own_t']={}
                    listvar['group_dg2zj23']['Other_Advatage_of_having_own_t']=str(specialcharremover(str(value)))
                elif key == 'group_dg2zj23/What_are_the_disadvantages_of_':#149
                    listvar['group_dg2zj23']['What_are_the_disadvantages_of_']={}
                    listvar['group_dg2zj23']['What_are_the_disadvantages_of_']=str(specialcharremover(str(value)))
                elif key == 'group_dg2zj23/Other_disadvantae_of_having_ow':#151
                    listvar['group_dg2zj23']['Other_disadvantae_of_having_ow']={}
                    listvar['group_dg2zj23']['Other_disadvantae_of_having_ow']=str(specialcharremover(str(value)))
                elif key == 'group_dg2zj23/Why_have_you_not_built_the_toi':#152
                    listvar['group_dg2zj23']['Why_have_you_not_built_the_toi']={}
                    listvar['group_dg2zj23']['Why_have_you_not_built_the_toi']=str(specialcharremover(str(value)))
                elif key == 'group_dg2zj23/Other_reason_why_you_have_not':#153
                    listvar['group_dg2zj23']['Other_reason_why_you_have_not']={}
                    listvar['group_dg2zj23']['Other_reason_why_you_have_not']=str(specialcharremover(str(value)))
                elif key == 'group_dg2zj23/From_amongst_the_family_member':#154
                    listvar['group_dg2zj23']['From_amongst_the_family_member']={}
                    listvar['group_dg2zj23']['From_amongst_the_family_member']=str(specialcharremover(str(value)))
                elif key == 'group_dg2zj23/Will_all_the_members_in_the_ho':#155
                    listvar['group_dg2zj23']['Will_all_the_members_in_the_ho']={}
                    listvar['group_dg2zj23']['Will_all_the_members_in_the_ho']=str(specialcharremover(str(value)))
                elif key == 'group_dg2zj23/Who_will_not_approve_it_Reco':#156
                    listvar['group_dg2zj23']['Who_will_not_approve_it_Reco']={}
                    listvar['group_dg2zj23']['Who_will_not_approve_it_Reco']=str(specialcharremover(str(value)))
                elif key == 'group_dg2zj23/What_are_the_efforts_taken_by_':#157
                    listvar['group_dg2zj23']['What_are_the_efforts_taken_by_']={}
                    listvar['group_dg2zj23']['What_are_the_efforts_taken_by_']=str(specialcharremover(str(value)))
                elif key == 'group_dg2zj23/Other_effort_to_clean_the_area':#158
                    listvar['group_dg2zj23']['Other_effort_to_clean_the_area']={}
                    listvar['group_dg2zj23']['Other_effort_to_clean_the_area']=str(specialcharremover(str(value)))
                elif key == 'group_dg2zj23/Do_you_have_sufficient_water_s':#159
                    listvar['group_dg2zj23']['Do_you_have_sufficient_water_s']={}
                    listvar['group_dg2zj23']['Do_you_have_sufficient_water_s']=str(specialcharremover(str(value)))
                elif key == 'group_dg2zj23/Are_you_willing_to_accept_indi':#160
                    listvar['group_dg2zj23']['Are_you_willing_to_accept_indi']={}
                    listvar['group_dg2zj23']['Are_you_willing_to_accept_indi']=str(specialcharremover(str(value)))
                elif key == 'group_dg2zj23/Will_your_bathroom_and_toilet_':#161
                    listvar['group_dg2zj23']['Will_your_bathroom_and_toilet_']={}
                    listvar['group_dg2zj23']['Will_your_bathroom_and_toilet_']=str(specialcharremover(str(value)))
                elif key == 'group_dg2zj23/Do_you_think_receiving_subsidy':#162
                    listvar['group_dg2zj23']['Do_you_think_receiving_subsidy']={}
                    listvar['group_dg2zj23']['Do_you_think_receiving_subsidy']=str(specialcharremover(str(value)))
                elif key == 'group_dg2zj23/How_do_you_want_to_receive_the':#163
                    listvar['group_dg2zj23']['How_do_you_want_to_receive_the']={}
                    listvar['group_dg2zj23']['How_do_you_want_to_receive_the']=str(specialcharremover(str(value)))
                elif key == 'group_dg2zj23/Reasons_for_opting_the_choice_':#164
                    listvar['group_dg2zj23']['Reasons_for_opting_the_choice_']={}
                    listvar['group_dg2zj23']['Reasons_for_opting_the_choice_']=str(specialcharremover(str(value)))
                elif key =="formhub/uuid":
                    listvar['formhub']['uuid']= {}
                    listvar['formhub']['uuid']=formhub_id
                elif key =='start':
                    listvar['start']={}
                    listvar['start']=value
                elif key == 'end':
                    listvar['end']={}
                    listvar['end']=value
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
                    id_id = value
                elif key =='_submission_time':
                    listvar['_submission_time']={}
                    listvar['_submission_time']=value
                elif key=="_xform_id_string":
                    listvar['_xform_id_string']= {}
                    listvar['_xform_id_string']=str(xform_id_string)
                elif key == '_submitted_by':
                    listvar['_submitted_by']={}
                    listvar['_submitted_by']=value
        xmldata=""
        xmldata = dict2xml({xform_id_string : listvar})
        xmlfinal=""
        xmlfinal=str(xmldata.display()).replace('<'+xform_id_string+'>','<'+xform_id_string+'  id="'+xform_id_string+'" version="'+versioncode+'">').replace('<_xform_id_string/>','')
        print xmlfinal
        filename=str("Impactdemo_"+city_id+"_"+admin_no+"_"+slum_no+"_"+house_no+"_"+ str(id_id)+".xml")
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
