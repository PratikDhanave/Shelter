import urllib
url = "https://survey.shelter-associates.org/media/ShelterPhotos/"+ "FactsheetPhotos/SlumView_127.jpg"
f = open("test.txt","w")
print url
f.write(url+"\n")
f.close()
string="FactsheetPhotos/SlumView_127.jpg"
urllib.urlretrieve(url,"FactsheetPhotos/SlumView_127.jpg")
		