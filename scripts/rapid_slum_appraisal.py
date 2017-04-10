import psycopg2

def imagemigration_NEW():
	count = 0
	slum = psycopg2.connect(database='shelter_migrate',user='shelter',password='Sh3lt3rAss0ciat3s',host='45.56.104.240',port='5432')
	cursor_slum = slum.cursor()
	cursor_slum.execute("select * from master_rapid_slum_appraisalmigrate4;")
	fetch_slum_code = cursor_slum.fetchall()
	for f in fetch_slum_code:
		id=f[0]
		slum_name =f[1]
		approximate_population=f[1]
		toilet_cost=f[3]
		toilet_seat_to_persons_ratio=f[4] 
		percentage_with_an_individual_water_connection=f[5]
		frequency_of_clearance_of_waste_containers=f[6]
		general_info_left_image=f[7]
		toilet_info_left_image=f[8]
		waste_management_info_left_image=f[9] 
		water_info_left_image=f[10]
		roads_and_access_info_left_image=f[11]
		drainage_info_left_image=f[12]
		gutter_info_left_image=f[13]
		general_image_bottomdown1=f[14]
		general_image_bottomdown2=f[15]
		toilet_image_bottomdown1=f[16]
		toilet_image_bottomdown2=f[17]
		waste_management_image_bottomdown1=f[18]
		waste_management_image_bottomdown2=f[19]
		water_image_bottomdown1=f[20] 
		water_image_bottomdown2=f[21]
		roads_image_bottomdown1=f[22]
		road_image_bottomdown2=f[23]
		drainage_image_bottomdown1=f[24]
		drainage_image_bottomdown2=f[25]
		gutter_image_bottomdown1=f[26]
		gutter_image_bottomdown2=f[27]
		shelter = psycopg2.connect(database='shelter_migrate',user='shelter',password='Sh3lt3rAss0ciat3s',host='45.56.104.240',port='5432')
		cursor_shelter_insert = shelter.cursor()
		query = "insert into master_rapid_slum_appraisal(slum_name_id,approximate_population,toilet_cost,toilet_seat_to_persons_ratio, percentage_with_an_individual_water_connection,frequency_of_clearance_of_waste_containers,general_info_left_image,toilet_info_left_image,waste_management_info_left_image, water_info_left_image,roads_and_access_info_left_image,drainage_info_left_image, gutter_info_left_image, general_image_bottomdown1, general_image_bottomdown2,toilet_image_bottomdown1, toilet_image_bottomdown2, waste_management_image_bottomdown1 ,waste_management_image_bottomdown2,water_image_bottomdown1, water_image_bottomdown2,roads_image_bottomdown1, road_image_bottomdown2,drainage_image_bottomdown1,drainage_image_bottomdown2 ,gutter_image_bottomdown1,gutter_image_bottomdown2) VALUES (%s,%s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s);"
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
			drainage_image_bottomdown2,
			gutter_image_bottomdown1,
			gutter_image_bottomdown2) 
		cursor_shelter_insert.execute(query,data)
		shelter.commit()
		print count
		count=count+1





if __name__ == "__main__":
	imagemigration_NEW()







