import psycopg2

def imagemigration_NEW():
	slum = psycopg2.connect(database='shelter_old',user='postgres',password='softcorner',host='localhost',port='5432')
	cursor_slum = slum.cursor()
	cursor_slum.execute("select slum_code ray_survey_slumsurveymetadata where;")
	fetch_slum_code = cursor_slum.fetchall()
	for i in fetch_slum_code:
		slum_id=i[0]
		print slum_id
		electoralward_id=i[1]
		print electoralward_id
		shelter = psycopg2.connect(database='django',user='postgres',password='softcorner',host='localhost',port='5432')
		cursor_shelter_insert = shelter.cursor()
		string = 'UPDATE master_slum SET electoral_ward_id='
		string_query = string + str(shelter_slum_code) + ' WHERE id=' + str(slum_id) +';'
		print string_query
		cursor_shelter_insert.execute(string_query)
		shelter.commit()

if __name__ == "__main__":
	imagemigration_NEW()







"""

			shelter = psycopg2.connect(database='shelter_migrate',user='shelter',password='Sh3lt3rAss0ciat3s',host='45.56.104.240',port='5432')
"""	
