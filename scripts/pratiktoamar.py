import psycopg2
import urllib

def imagemigration2():
	slum = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
	cursor_slum = slum.cursor()
	cursor_slum.execute("select slum_id from ray_survey_slumsurveymetadata where survey_id=13;")
	fetch_slum_ids = cursor_slum.fetchall()
	for i in fetch_slum_ids:
		id = i[0]
		str_id=str(id)	        
		GeneralQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_GeneralQ = GeneralQ.cursor()
		cursor_GeneralQ.execute("select id from  ray_survey_reporttemplatedesiredfact where  template_desiredfact_id=60 and desired_fact_group_id='34' and report_id=2;")
		fetch_data1 = cursor_GeneralQ.fetchone()
		GeneralQ_id = fetch_data1[0]
		GeneralA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_GeneralA = GeneralA.cursor()
		strQ_id=str(GeneralQ_id)
		GeneralA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_GeneralA = GeneralA.cursor()
		string = 'select image_name from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_GeneralA.execute(string_query)	
		General_image = cursor_GeneralA.fetchone()		
		print General_image
		url = "https://survey.shelter-associates.org/media/" + General_image
		urllib.urlretrieve(url,General_image)
		ToiletQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_ToiletQ = ToiletQ.cursor()
		cursor_ToiletQ.execute("select id from  ray_survey_reporttemplatedesiredfact where  template_desiredfact_id=60 and desired_fact_group_id='35' and report_id=2;")
		fetch_data2 = cursor_ToiletQ.fetchone()
		ToiletQ_id = fetch_data2[0]
		ToiletA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_ToiletA = ToiletA.cursor()
		strQ_id=str(ToiletQ_id)
		ToiletA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_ToiletA = ToiletA.cursor()
		string = 'select image_name from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_ToiletA.execute(string_query)	
		Toilet_image = cursor_ToiletA.fetchone()
		print Toilet_image
		url = "https://survey.shelter-associates.org/media/" + Toilet_image
		urllib.urlretrieve(url,Toilet_image)		
		waterQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_waterQ = waterQ.cursor()
		cursor_waterQ.execute("select id from  ray_survey_reporttemplatedesiredfact where  template_desiredfact_id=60 and desired_fact_group_id='36' and report_id=2;")
		fetch_data3 = cursor_waterQ.fetchone()
		waterQ_id = fetch_data3[0]
		waterA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_waterA = waterA.cursor()
		strQ_id=str(waterQ_id)
		waterA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_waterA = waterA.cursor()
		string = 'select image_name from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_waterA.execute(string_query)	
		water_image = cursor_waterA.fetchone()
		print water_image
		url = "https://survey.shelter-associates.org/media/" + water_image
		urllib.urlretrieve(url,water_image)				
		wasteQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_wasteQ = wasteQ.cursor()
		cursor_wasteQ.execute("select id from  ray_survey_reporttemplatedesiredfact where  template_desiredfact_id=60 and desired_fact_group_id='37' and report_id=2;")
		fetch_data4 = cursor_wasteQ.fetchone()
		wasteQ_id = fetch_data4[0]
		wasteA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_wasteA = wasteA.cursor()
		strQ_id=str(wasteQ_id)
		wasteA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_wasteA = wasteA.cursor()
		string = 'select image_name from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_wasteA.execute(string_query)	
		waste_image = cursor_wasteA.fetchone()
		print waste_image
		url = "https://survey.shelter-associates.org/media/" + waste_image
		urllib.urlretrieve(url,waste_image)						
		roadQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_roadQ = roadQ.cursor()
		cursor_roadQ.execute("select id from  ray_survey_reporttemplatedesiredfact where  template_desiredfact_id=60 and desired_fact_group_id='39' and report_id=2;")
		fetch_data5 = cursor_roadQ.fetchone()
		roadQ_id = fetch_data5[0]
		roadA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_roadA = roadA.cursor()
		strQ_id=str(roadQ_id)
		roadA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_roadA = wasteA.cursor()
		string = 'select image_name from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_roadA.execute(string_query)	
		road_image = cursor_roadA.fetchone()
		print road_image
		url = "https://survey.shelter-associates.org/media/" + road_image
		urllib.urlretrieve(url,road_image)								
		drainageQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_drainageQ = drainageQ.cursor()
		cursor_drainageQ.execute("select id from  ray_survey_reporttemplatedesiredfact where  template_desiredfact_id=60 and desired_fact_group_id='40' and report_id=2;")
		fetch_data6 = cursor_drainageQ.fetchone()
		drainageQ_id = fetch_data6[0]
		drainageA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_drainageA = drainageA.cursor()
		strQ_id=str(drainageQ_id)
		drainageA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_drainageA = drainageA.cursor()
		string = 'select image_name from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_drainageA.execute(string_query)	
		drainage_image = cursor_drainageA.fetchone()
		print drainage_image
		url = "https://survey.shelter-associates.org/media/" + drainage_image
		urllib.urlretrieve(url,drainage_image)										
		ApproxPQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_ApproxPQ = ApproxPQ.cursor()
		cursor_ApproxPQ.execute("select * from ray_survey_reporttemplatedesiredfact where template_desiredfact_id=13 and report_id=2;")
		fetch_data8 = cursor_ApproxPQ.fetchone()
		ApproxPQ_id = fetch_data8[0]
		ApproxPA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_ApproxPA = ApproxPA.cursor()
		strQ_id=str(ApproxPQ_id)
		ApproxPA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_ApproxPA = ApproxPA.cursor()
		string = 'select text from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_ApproxPA.execute(string_query)	
		ApproxP = cursor_ApproxPA.fetchone()
		print ApproxP
		TratioQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_TratioQ = TratioQ.cursor()
		cursor_TratioQ.execute("select * from ray_survey_reporttemplatedesiredfact where template_desiredfact_id=18 and report_id=2 ;")
		fetch_data9 = cursor_TratioQ.fetchone()
		TratioQ_id = fetch_data9[0]
		TratioA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_TratioA = TratioA.cursor()
		strQ_id=str(TratioQ_id)
		TratioA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_TratioA = TratioA.cursor()
		string = 'select text from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_TratioA.execute(string_query)	
		Tratio = cursor_TratioA.fetchone()
		print Tratio
		FCWCQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_FCWCQ = FCWCQ.cursor()
		cursor_FCWCQ.execute("select * from ray_survey_reporttemplatedesiredfact where template_desiredfact_id=18 and report_id=2 ;")
		fetch_data10 = cursor_FCWCQ.fetchone()
		FCWCQ_id = fetch_data10[0]
		FCWCA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_FCWCA = FCWCA.cursor()
		strQ_id=str(FCWCQ_id)
		FCWCA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_FCWCA = FCWCA.cursor()
		string = 'select text from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_FCWCA.execute(string_query)	
		FCWC = cursor_FCWCA.fetchone()
		print FCWC
		PWIWCQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_PWIWCQ = PWIWCQ.cursor()
		cursor_PWIWCQ.execute("select * from ray_survey_reporttemplatedesiredfact where template_desiredfact_id=78 and report_id=2 ;")
		fetch_data11 = cursor_PWIWCQ.fetchone()
		PWIWCQ_id = fetch_data11[0]
		PWIWCA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_PWIWCA = PWIWCA.cursor()
		strQ_id=str(PWIWCQ_id)
		PWIWCA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_PWIWCA = PWIWCA.cursor()
		string = 'select text from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_PWIWCA.execute(string_query)	
		PWIWC = cursor_PWIWCA.fetchone()
		print PWIWC
		TcostQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_TcostQ = TcostQ.cursor()
		cursor_TcostQ.execute("select * from ray_survey_reporttemplatedesiredfact where template_desiredfact_id=78 and report_id=2 ;")
		fetch_data12 = cursor_TcostQ.fetchone()
		TcostQ_id = fetch_data12[0]
		TcostA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_TcostA = TcostA.cursor()
		strQ_id=str(TcostQ_id)
		TcostA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_TcostA = TcostA.cursor()
		string = 'select text from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_TcostA.execute(string_query)	
		Tcost = cursor_TcostA.fetchone()
		print Tcost
		BottomDownQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownQ = BottomDownQ.cursor()
		cursor_BottomDownQ.execute("select id from ray_survey_reporttemplatedesiredfact where  template_desiredfact_id=62 and desired_fact_group_id='35' and report_id=2;")
		fetch_data1 = cursor_BottomDownQ.fetchone()
		BottomDownQ_id = fetch_data1[0]
		BottomDownA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownA = BottomDownA.cursor()
		strQ_id=str(BottomDownQ_id)
		BottomDownA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownA = BottomDownA.cursor()
		string = 'select fact_image_id from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_BottomDownA.execute(string_query)	
		BottomDown = cursor_BottomDownA.fetchall()
		print BottomDown
		print type(BottomDown)
		if not BottomDown:
			BottomDownright_image1_toilet=''
			BottomDownright_image2_toilet=''
  			print "List is empty"
		else:
			if(len(BottomDown)==1):
				BottomDownright1_id1 = BottomDown[0][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image1_toilet = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image1_toilet
				url = "https://survey.shelter-associates.org/media/" + BottomDownright_image1_toilet
				urllib.urlretrieve(url,BottomDownright_image1_toilet)
				BottomDownright_image2_toilet=''
			else:    
				print "List has 2 element"
				print BottomDown[0][0]
				print BottomDown[1][0]
				BottomDownright1_id1 = BottomDown[0][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image1_toilet = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image1_toilet
				url = "https://survey.shelter-associates.org/media/" + BottomDownright_image1_toilet
				urllib.urlretrieve(url,BottomDownright_image1_toilet)
				BottomDownright1_id2 = BottomDown[1][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image2_toilet = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image2_toilet
				url = "https://survey.shelter-associates.org/media/" + BottomDownright_image2_toilet
				urllib.urlretrieve(url,BottomDownright_image2_toilet)
		BottomDownQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownQ = BottomDownQ.cursor()
		cursor_BottomDownQ.execute("select id from ray_survey_reporttemplatedesiredfact where  template_desiredfact_id=62 and desired_fact_group_id='36' and report_id=2;")
		fetch_data1 = cursor_BottomDownQ.fetchone()
		BottomDownQ_id = fetch_data1[0]
		BottomDownA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownA = BottomDownA.cursor()
		strQ_id=str(BottomDownQ_id)
		BottomDownA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownA = BottomDownA.cursor()
		string = 'select fact_image_id from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_BottomDownA.execute(string_query)	
		BottomDown = cursor_BottomDownA.fetchall()
		print BottomDown
		print type(BottomDown)
		if not BottomDown:
			BottomDownright_image1_water=''
			BottomDownright_image2_water=''
  			print "List is empty"
		else:
			if(len(BottomDown)==1):
				BottomDownright1_id1 = BottomDown[0][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image1_water = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image1_water
				BottomDownright_image2_water=''
				url = "https://survey.shelter-associates.org/media/" + BottomDownright_image1_water
				urllib.urlretrieve(url,BottomDownright_image1_water)
			else:    
				print "List has 2 element"
				print BottomDown[0][0]
				print BottomDown[1][0]
				BottomDownright1_id1 = BottomDown[0][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image1_water = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image1_water
				url = "https://survey.shelter-associates.org/media/" + BottomDownright_image1_water
				urllib.urlretrieve(url,BottomDownright_image1_water)
				BottomDownright1_id2 = BottomDown[1][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image2_water = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image2_water
				url = "https://survey.shelter-associates.org/media/" + BottomDownright_image2_water
				urllib.urlretrieve(url,BottomDownright_image2_water)
		BottomDownQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownQ = BottomDownQ.cursor()
		cursor_BottomDownQ.execute("select id from ray_survey_reporttemplatedesiredfact where  template_desiredfact_id=62 and desired_fact_group_id='37' and report_id=2;")
		fetch_data1 = cursor_BottomDownQ.fetchone()
		BottomDownQ_id = fetch_data1[0]
		BottomDownA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownA = BottomDownA.cursor()
		strQ_id=str(BottomDownQ_id)
		BottomDownA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownA = BottomDownA.cursor()
		string = 'select fact_image_id from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_BottomDownA.execute(string_query)	
		BottomDown = cursor_BottomDownA.fetchall()
		print BottomDown
		print type(BottomDown)
		if not BottomDown:
			BottomDownright_image1_waste=''
			BottomDownright_image2_waste=''
  			print "List is empty"
		else:
			if(len(BottomDown)==1):
				BottomDownright1_id1 = BottomDown[0][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image1_waste = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image1_waste
				BottomDownright_image2_waste =''
				url = "https://survey.shelter-associates.org/media/" + BottomDownright_image1_waste
				urllib.urlretrieve(url,BottomDownright_image1_waste)
			else:    
				print "List has 2 element"
				print BottomDown[0][0]
				print BottomDown[1][0]
				BottomDownright1_id1 = BottomDown[0][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image1_waste = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image1_waste
				url = "https://survey.shelter-associates.org/media/" + BottomDownright_image1_waste
				urllib.urlretrieve(url,BottomDownright_image1_waste)
				BottomDownright1_id2 = BottomDown[1][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image2_waste = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image2_waste
				url = "https://survey.shelter-associates.org/media/" + BottomDownright_image2_waste
				urllib.urlretrieve(url,BottomDownright_image2_waste)
		BottomDownQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownQ = BottomDownQ.cursor()
		cursor_BottomDownQ.execute("select id from ray_survey_reporttemplatedesiredfact where  template_desiredfact_id=62 and desired_fact_group_id='39' and report_id=2;")
		fetch_data1 = cursor_BottomDownQ.fetchone()
		BottomDownQ_id = fetch_data1[0]
		BottomDownA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownA = BottomDownA.cursor()
		strQ_id=str(BottomDownQ_id)
		BottomDownA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownA = BottomDownA.cursor()
		string = 'select fact_image_id from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_BottomDownA.execute(string_query)	
		BottomDown = cursor_BottomDownA.fetchall()
		print BottomDown
		print type(BottomDown)
		if not BottomDown:
			BottomDownright_image1_road=''
			BottomDownright_image2_road=''
  			print "List is empty"
		else:
			if(len(BottomDown)==1):
				BottomDownright1_id1 = BottomDown[0][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image1_road = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image1_road
				BottomDownright_image2_road =''
				url = "https://survey.shelter-associates.org/media/" + BottomDownright_image1_road
				urllib.urlretrieve(url,BottomDownright_image1_road)
			else:    
				print "List has 2 element"
				print BottomDown[0][0]
				print BottomDown[1][0]
				BottomDownright1_id1 = BottomDown[0][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image1_road = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image1_road
				url = "https://survey.shelter-associates.org/media/" + BottomDownright_image1_road
				urllib.urlretrieve(url,BottomDownright_image1_road)
				BottomDownright1_id2 = BottomDown[1][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image2_road = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image2_road
				url = "https://survey.shelter-associates.org/media/" + BottomDownright_image2_road
				urllib.urlretrieve(url,BottomDownright_image2_road)
		BottomDownQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownQ = BottomDownQ.cursor()
		cursor_BottomDownQ.execute("select id from ray_survey_reporttemplatedesiredfact where  template_desiredfact_id=62 and desired_fact_group_id='40' and report_id=2;")
		fetch_data1 = cursor_BottomDownQ.fetchone()
		BottomDownQ_id = fetch_data1[0]
		BottomDownA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownA = BottomDownA.cursor()
		strQ_id=str(BottomDownQ_id)
		BottomDownA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownA = BottomDownA.cursor()
		string = 'select fact_image_id from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_BottomDownA.execute(string_query)	
		BottomDown = cursor_BottomDownA.fetchall()
		print BottomDown
		print type(BottomDown)
		if not BottomDown:
			BottomDownright_image1_drainage=''
			BottomDownright_image2_drainage=''
  			print "List is empty"
		else:
			if(len(BottomDown)==1):
				BottomDownright1_id1 = BottomDown[0][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image1_drainage = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image1_drainage
				BottomDownright_image2_drainage=''
			else:    
				print "List has 2 element"
				print BottomDown[0][0]
				print BottomDown[1][0]
				BottomDownright1_id1 = BottomDown[0][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image1_drainage = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image1_drainage
				url = "https://survey.shelter-associates.org/media/" + BottomDownright_image1_waste
				urllib.urlretrieve(url,BottomDownright_image1_drainage)
				BottomDownright1_id2 = BottomDown[1][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image2_drainage = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image2_drainage
				url = "https://survey.shelter-associates.org/media/" + BottomDownright_image2_waste
				urllib.urlretrieve(url,BottomDownright_image2_drainage)						
		slum_name = id
		approximate_population = ApproxP
		toilet_cost= Tcost
		toilet_seat_to_persons_ratio = Tratio
		percentage_with_an_individual_water_connection = PWIWC
		frequency_of_clearance_of_waste_containers = FCWC
		general_info_left_image = General_image
		toilet_info_left_image = Toilet_image
		waste_management_info_left_image = waste_image
		water_info_left_image = water_image
		roads_and_access_info_left_image = road_image
		drainage_info_left_image = drainage_image
		gutter_image = drainage_image 
		gutter_info_left_image = gutter_image
		general_image_bottomdown1 = gutter_image
		general_image_bottomdown2 = gutter_image
		toilet_image_bottomdown1 = BottomDownright_image1_toilet
		toilet_image_bottomdown2 = BottomDownright_image2_toilet
		waste_management_image_bottomdown1 = BottomDownright_image1_waste
		waste_management_image_bottomdown2 = BottomDownright_image2_waste
		water_image_bottomdown1 = BottomDownright_image1_water
		water_image_bottomdown2 = BottomDownright_image2_water
		roads_image_bottomdown1 = BottomDownright_image1_road
		road_image_bottomdown2 = BottomDownright_image2_road  
		drainage_image_bottomdown1 = BottomDownright_image1_drainage 
		drainage_image_bottomdown2 = BottomDownright_image2_drainage
		shelter = psycopg2.connect(database='django',user='postgres',password='softcorner',host='127.0.0.1',port='5432')
		cursor_shelter_insert = shelter.cursor()
		query = "insert into master_rapid_slum_appraisalmigrate5 (slum_name_id,approximate_population,toilet_cost,toilet_seat_to_persons_ratio, percentage_with_an_individual_water_connection,frequency_of_clearance_of_waste_containers,general_info_left_image,toilet_info_left_image,waste_management_info_left_image, water_info_left_image,roads_and_access_info_left_image,drainage_info_left_image, gutter_info_left_image, general_image_bottomdown1, general_image_bottomdown2,toilet_image_bottomdown1, toilet_image_bottomdown2, waste_management_image_bottomdown1 ,waste_management_image_bottomdown2,water_image_bottomdown1, water_image_bottomdown2,roads_image_bottomdown1, road_image_bottomdown2,drainage_image_bottomdown1,drainage_image_bottomdown2 ) VALUES (%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s);"
		data=(slum_name,
			approximate_population,
			toilet_cost,
			toilet_seat_to_persons_ratio, 
			percentage_with_an_individual_water_connection,
			frequency_of_clearance_of_waste_containers,
			general_info_left_image,
			toilet_info_left_image, 
			waste_management_info_left_image, 
			water_info_left_image, 
			roads_and_access_info_left_image,
			drainage_info_left_image,
			gutter_info_left_image,
			general_image_bottomdown1, 
			general_image_bottomdown2, 
			toilet_image_bottomdown1, 
			toilet_image_bottomdown2,
			waste_management_image_bottomdown1 ,
			waste_management_image_bottomdown2,
			water_image_bottomdown1, 
			water_image_bottomdown2,
			roads_image_bottomdown1,
			road_image_bottomdown2,
			drainage_image_bottomdown1,
			drainage_image_bottomdown2) 
		cursor_shelter_insert.execute(query,data)
		shelter.commit()

"""

def imagination():
	slum = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
	cursor_slum = slum.cursor()
	cursor_slum.execute("select slum_id from ray_survey_slumsurveymetadata where survey_id=13;")
	fetch_slum_ids = cursor_slum.fetchall()
	for i in fetch_slum_ids:
		id = i[0]
		str_id=str(id)	        
		ApproxPQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_ApproxPQ = ApproxPQ.cursor()
		cursor_ApproxPQ.execute("select * from ray_survey_reporttemplatedesiredfact where template_desiredfact_id=13 and report_id=2;")
		fetch_data8 = cursor_ApproxPQ.fetchone()
		ApproxPQ_id = fetch_data8[0]
		ApproxPA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_ApproxPA = ApproxPA.cursor()
		strQ_id=str(ApproxPQ_id)
		ApproxPA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_ApproxPA = ApproxPA.cursor()
		string = 'select text from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_ApproxPA.execute(string_query)	
		ApproxP = cursor_ApproxPA.fetchone()
		print ApproxP
		TratioQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_TratioQ = TratioQ.cursor()
		cursor_TratioQ.execute("select * from ray_survey_reporttemplatedesiredfact where template_desiredfact_id=18 and report_id=2 ;")
		fetch_data9 = cursor_TratioQ.fetchone()
		TratioQ_id = fetch_data9[0]
		TratioA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_TratioA = TratioA.cursor()
		strQ_id=str(TratioQ_id)
		TratioA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_TratioA = TratioA.cursor()
		string = 'select text from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_TratioA.execute(string_query)	
		Tratio = cursor_TratioA.fetchone()
		print Tratio
		FCWCQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_FCWCQ = FCWCQ.cursor()
		cursor_FCWCQ.execute("select * from ray_survey_reporttemplatedesiredfact where template_desiredfact_id=18 and report_id=2 ;")
		fetch_data10 = cursor_FCWCQ.fetchone()
		FCWCQ_id = fetch_data10[0]
		FCWCA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_FCWCA = FCWCA.cursor()
		strQ_id=str(FCWCQ_id)
		FCWCA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_FCWCA = FCWCA.cursor()
		string = 'select text from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_FCWCA.execute(string_query)	
		FCWC = cursor_FCWCA.fetchone()
		print FCWC
		PWIWCQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_PWIWCQ = PWIWCQ.cursor()
		cursor_PWIWCQ.execute("select * from ray_survey_reporttemplatedesiredfact where template_desiredfact_id=78 and report_id=2 ;")
		fetch_data11 = cursor_PWIWCQ.fetchone()
		PWIWCQ_id = fetch_data11[0]
		PWIWCA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_PWIWCA = PWIWCA.cursor()
		strQ_id=str(PWIWCQ_id)
		PWIWCA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_PWIWCA = PWIWCA.cursor()
		string = 'select text from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_PWIWCA.execute(string_query)	
		PWIWC = cursor_PWIWCA.fetchone()
		print PWIWC
		TcostQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_TcostQ = TcostQ.cursor()
		cursor_TcostQ.execute("select * from ray_survey_reporttemplatedesiredfact where template_desiredfact_id=78 and report_id=2 ;")
		fetch_data12 = cursor_TcostQ.fetchone()
		TcostQ_id = fetch_data12[0]
		TcostA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_TcostA = TcostA.cursor()
		strQ_id=str(TcostQ_id)
		TcostA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_TcostA = TcostA.cursor()
		string = 'select text from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_TcostA.execute(string_query)	
		Tcost = cursor_TcostA.fetchone()
		print Tcost





def imagination2_toilet():
	slum = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
	cursor_slum = slum.cursor()
	cursor_slum.execute("select slum_id from ray_survey_slumsurveymetadata where survey_id=13;")
	fetch_slum_ids = cursor_slum.fetchall()
	for i in fetch_slum_ids:
		id = i[0]
		str_id=str(id)	        
		BottomDownQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownQ = BottomDownQ.cursor()
		cursor_BottomDownQ.execute("select id from ray_survey_reporttemplatedesiredfact where  template_desiredfact_id=62 and desired_fact_group_id='35' and report_id=2;")
		fetch_data1 = cursor_BottomDownQ.fetchone()
		BottomDownQ_id = fetch_data1[0]
		BottomDownA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownA = BottomDownA.cursor()
		strQ_id=str(BottomDownQ_id)
		BottomDownA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownA = BottomDownA.cursor()
		string = 'select fact_image_id from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_BottomDownA.execute(string_query)	
		BottomDown = cursor_BottomDownA.fetchall()
		print BottomDown
		print type(BottomDown)
		if not BottomDown:
  			print "List is empty"
		else:
			if(len(BottomDown)==1):
				BottomDownright1_id1 = BottomDown[0][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image1_toilet = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image1_toilet
			else:    
				print "List has 2 element"
				print BottomDown[0][0]
				print BottomDown[1][0]
				BottomDownright1_id1 = BottomDown[0][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image1_toilet = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image1_toilet
				BottomDownright1_id2 = BottomDown[1][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image2_toilet = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image2_toilet		


def imagination3_water():
	slum = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
	cursor_slum = slum.cursor()
	cursor_slum.execute("select slum_id from ray_survey_slumsurveymetadata where survey_id=13;")
	fetch_slum_ids = cursor_slum.fetchall()
	for i in fetch_slum_ids:
		id = i[0]
		str_id=str(id)	        
		BottomDownQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownQ = BottomDownQ.cursor()
		cursor_BottomDownQ.execute("select id from ray_survey_reporttemplatedesiredfact where  template_desiredfact_id=62 and desired_fact_group_id='36' and report_id=2;")
		fetch_data1 = cursor_BottomDownQ.fetchone()
		BottomDownQ_id = fetch_data1[0]
		BottomDownA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownA = BottomDownA.cursor()
		strQ_id=str(BottomDownQ_id)
		BottomDownA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownA = BottomDownA.cursor()
		string = 'select fact_image_id from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_BottomDownA.execute(string_query)	
		BottomDown = cursor_BottomDownA.fetchall()
		print BottomDown
		print type(BottomDown)
		if not BottomDown:
  			print "List is empty"
		else:
			if(len(BottomDown)==1):
				BottomDownright1_id1 = BottomDown[0][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image1_water = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image1_water
			else:    
				print "List has 2 element"
				print BottomDown[0][0]
				print BottomDown[1][0]
				BottomDownright1_id1 = BottomDown[0][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image1_water = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image1_water
				BottomDownright1_id2 = BottomDown[1][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image2_water = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image2_water		



def imagination3_waste():
	slum = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
	cursor_slum = slum.cursor()
	cursor_slum.execute("select slum_id from ray_survey_slumsurveymetadata where survey_id=13;")
	fetch_slum_ids = cursor_slum.fetchall()
	for i in fetch_slum_ids:
		id = i[0]
		str_id=str(id)	        
		BottomDownQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownQ = BottomDownQ.cursor()
		cursor_BottomDownQ.execute("select id from ray_survey_reporttemplatedesiredfact where  template_desiredfact_id=62 and desired_fact_group_id='37' and report_id=2;")
		fetch_data1 = cursor_BottomDownQ.fetchone()
		BottomDownQ_id = fetch_data1[0]
		BottomDownA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownA = BottomDownA.cursor()
		strQ_id=str(BottomDownQ_id)
		BottomDownA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownA = BottomDownA.cursor()
		string = 'select fact_image_id from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_BottomDownA.execute(string_query)	
		BottomDown = cursor_BottomDownA.fetchall()
		print BottomDown
		print type(BottomDown)
		if not BottomDown:
  			print "List is empty"
		else:
			if(len(BottomDown)==1):
				BottomDownright1_id1 = BottomDown[0][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image1_waste = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image1_waste
			else:    
				print "List has 2 element"
				print BottomDown[0][0]
				print BottomDown[1][0]
				BottomDownright1_id1 = BottomDown[0][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image1_waste = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image1_waste
				BottomDownright1_id2 = BottomDown[1][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image2_waste = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image2_waste		




def imagination3_road():
	slum = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
	cursor_slum = slum.cursor()
	cursor_slum.execute("select slum_id from ray_survey_slumsurveymetadata where survey_id=13;")
	fetch_slum_ids = cursor_slum.fetchall()
	for i in fetch_slum_ids:
		id = i[0]
		str_id=str(id)	        
		BottomDownQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownQ = BottomDownQ.cursor()
		cursor_BottomDownQ.execute("select id from ray_survey_reporttemplatedesiredfact where  template_desiredfact_id=62 and desired_fact_group_id='39' and report_id=2;")
		fetch_data1 = cursor_BottomDownQ.fetchone()
		BottomDownQ_id = fetch_data1[0]
		BottomDownA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownA = BottomDownA.cursor()
		strQ_id=str(BottomDownQ_id)
		BottomDownA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownA = BottomDownA.cursor()
		string = 'select fact_image_id from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_BottomDownA.execute(string_query)	
		BottomDown = cursor_BottomDownA.fetchall()
		print BottomDown
		print type(BottomDown)
		if not BottomDown:
  			print "List is empty"
		else:
			if(len(BottomDown)==1):
				BottomDownright1_id1 = BottomDown[0][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image1_road = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image1_road
			else:    
				print "List has 2 element"
				print BottomDown[0][0]
				print BottomDown[1][0]
				BottomDownright1_id1 = BottomDown[0][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image1_road = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image1_road
				BottomDownright1_id2 = BottomDown[1][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image2_road = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image2_road	






def imagination3_drainage():
	slum = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
	cursor_slum = slum.cursor()
	cursor_slum.execute("select slum_id from ray_survey_slumsurveymetadata where survey_id=13;")
	fetch_slum_ids = cursor_slum.fetchall()
	for i in fetch_slum_ids:
		id = i[0]
		str_id=str(id)	        
		BottomDownQ = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownQ = BottomDownQ.cursor()
		cursor_BottomDownQ.execute("select id from ray_survey_reporttemplatedesiredfact where  template_desiredfact_id=62 and desired_fact_group_id='40' and report_id=2;")
		fetch_data1 = cursor_BottomDownQ.fetchone()
		BottomDownQ_id = fetch_data1[0]
		BottomDownA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownA = BottomDownA.cursor()
		strQ_id=str(BottomDownQ_id)
		BottomDownA = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_BottomDownA = BottomDownA.cursor()
		string = 'select fact_image_id from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id='
		string_query = string + strQ_id + ' and slum_id=' + str_id +';'
		cursor_BottomDownA.execute(string_query)	
		BottomDown = cursor_BottomDownA.fetchall()
		print BottomDown
		print type(BottomDown)
		if not BottomDown:
  			print "List is empty"
		else:
			if(len(BottomDown)==1):
				BottomDownright1_id1 = BottomDown[0][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image1_drainage = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image1_drainage
			else:    
				print "List has 2 element"
				print BottomDown[0][0]
				print BottomDown[1][0]
				BottomDownright1_id1 = BottomDown[0][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image1_drainage = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image1_drainage
				BottomDownright1_id2 = BottomDown[1][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image2_drainage = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image2_drainage	

"""

if __name__ == "__main__":
	imagemigration2()
 