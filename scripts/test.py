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
		if not General_image:
			pass
		else:
		    print General_image[0]
		    try:
		    	url = "https://survey.shelter-associates.org/media/" + General_image[0]
		    	urllib.urlretrieve(url,General_image[0])
		    except:
		    	pass
			
	

		


if __name__ == "__main__":
	imagemigration2()
