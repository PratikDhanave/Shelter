import psycopg2

def value():
	shelter = psycopg2.connect(database='onadata1',user='shelter',password='Sh3lt3rAss0ciat3s',host='45.56.104.240',port='5432')
	cursor_shelter = shelter.cursor()
	cursor_shelter.execute("select * from logger_instance where xform_id='106' and id =9;")
	data = cursor_shelter.fetchone()
	print data
		
if __name__ == "__main__":
	value()



