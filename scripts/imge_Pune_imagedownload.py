import psycopg2
import urllib

def imagemigration2():
	url = "https://survey.shelter-associates.org/media/"
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
		if not General_image:
			General_imageV=""
		else:
			General_imageV=General_image[0]			
		print type(General_imageV)
		download_string=General_imageV
		final_url = url + download_string
		urllib.urlretrieve(final_url,download_string)		
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
		if not Toilet_image:
			Toilet_imageV=""
		else:
			Toilet_imageV=Toilet_image[0]			
		print type(Toilet_imageV)
		download_string=Toilet_imageV
		final_url = url + download_string
		urllib.urlretrieve(final_url,download_string)
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
		if not water_image:
			water_imageV=""
		else:
			water_imageV=water_image[0]			
		print type(water_imageV)
		download_string=water_imageV
		final_url = url + download_string
		urllib.urlretrieve(final_url,download_string)		
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
		if not waste_image:
			waste_imageV=""
		else:
			waste_imageV=waste_image[0]			
		print type(waste_imageV)
		download_string=waste_imageV
		final_url = url + download_string
		urllib.urlretrieve(final_url,download_string)				
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
		if not road_image:
			road_imageV=""
		else:
			road_imageV=road_image[0]			
		print type(road_imageV)
		download_string=road_imageV
		final_url = url + download_string
		urllib.urlretrieve(final_url,download_string)						
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
		if not road_image:
			drainage_imageV=""
		else:
			drainage_imageV=drainage_image[0]			
		print type(drainage_imageV)
		download_string=drainage_imageV
		final_url = url + download_string
		urllib.urlretrieve(final_url,download_string)								
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
				BottomDownright1_id2 = BottomDown[1][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image2_toilet = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image2_toilet
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
				BottomDownright_image2_waste=''
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
				BottomDownright1_id2 = BottomDown[1][0]
				BottomDownright1A = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
				cursor_BottomDownright1A = BottomDownright1A.cursor()
				string = 'select image_name from ray_survey_factimage where id='
				string_query = string + str(BottomDownright1_id1) +';'
				cursor_BottomDownright1A.execute(string_query)	
				BottomDownright_image2_drainage = cursor_BottomDownright1A.fetchone()
				print BottomDownright_image2_drainage
										



if __name__ == "__main__":
    imagemigration2()
 







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
