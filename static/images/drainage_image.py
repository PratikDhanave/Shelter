import psycopg2
import urllib


def main():
    image_download()
    pass

def drainage():
    old = psycopg2.connect(database='sheltersurvey',user='shelter',password='XIcfe4cIV7ooGiIb',host='176.58.119.87',port='5432')
    cursor_old = old.cursor()
    cursor_old.execute("select * from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id=53;")
    fetch_data = cursor_old.fetchall()
    for f in fetch_data:
	slum_name_id = f[2]
	drainage_image= f[4]
        shelter = psycopg2.connect(database='django',user='postgres',password='softcorner',host='127.0.0.1',port='5432')
        cursor_shelter_insert = shelter.cursor()
        query = "insert into master_drainage (slum_name_id,drainage_image) VALUES (%s ,%s);"
        data = (slum_name_id,drainage_image)
        cursor_shelter_insert.execute(query,data)
        shelter.commit()


def image_download():
    shelter = psycopg2.connect(database='sheltersurvey',user='shelter',password='XIcfe4cIV7ooGiIb',host='176.58.119.87',port='5432')
    cursor_shelter = shelter.cursor()
    query = "select * from ray_survey_reporttemplatefact where reporttemplate_desiredfact_id=53;" 
    cursor_shelter.execute(query)
    cursor_shelter_data = cursor_shelter.fetchall()
    count = 0    
    for f in cursor_shelter_data:
        drainage_image = str(f[4])
	print drainage_image
	#download_string = (drainage_image)
        url = "https://survey.shelter-associates.org/media/"
        final_url = str(url) + str(drainage_image)
        print str(final_url)	
        
        








"""
	
	download_string = (drainage_image)
        url = "https://survey.shelter-associates.org/media/"
        final_url = url + str(download_string)
        print final_url	
        if(download_string):
            urllib.urlretrieve(final_url,download_string)
 	    count = count + 1
    print count
"""

if __name__ == "__main__":
    main()
