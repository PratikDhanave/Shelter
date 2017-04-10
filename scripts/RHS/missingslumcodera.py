import psycopg2

def imagemigration_NEW():
	count = 0
	SList=[272538754114,272538754305,272538752105,272538755705,272538750305,272538755703,272538750202,2725387204,272538750407,272538755704,272538750404,272538750303,272538750406,272538754110,272538750403,272538754112,272538750402,272538750405]
	Slum_Code_List = []
	slum = psycopg2.connect(database='shelter_migrate',user='shelter',password='Sh3lt3rAss0ciat3s',host='45.56.104.240',port='5432')
	cursor_slum = slum.cursor()
	cursor_slum.execute("select shelter_slum_code from master_slum;")
	fetch_slum_code = cursor_slum.fetchall()
	for i in fetch_slum_code:
		print i[0]
		print Slum_Code_List.append(i[0])
	for i in SList:
		for j in Slum_Code_List:
			if(i==j):
				print("Matched",i)
			else:
				print "not found"
				count = count + 1
	print count
	print len(Slum_Code_List)


def Slum_list():
	slum_code_list = []
	old = psycopg2.connect(database='old1',user='postgres',password='softcorner',host='localhost',port='5432')
	cursor_old = old.cursor()
	cursor_old.execute("select id from ray_survey_slumsurveymetadata where slum_code in ('272538754114','272538754305','272538752105','272538755705','272538750305','272538755703','272538750202','2725387204','272538750407','272538755704','272538750404','272538750303', '272538750406','272538754110','272538750403','272538754112','272538750402','272538750405');")
	fetch_data = cursor_old.fetchall()
	for f in fetch_data:
		slum_code_list.append(f[0])
	print slum_code_list
	slum_code =  list(set(slum_code_list))
    print slum_code
if __name__ == "__main__":
	Slum_list()
