from pykml import parser
import json


def FinalHouses_Ambedkar_Nagar():
    fo = open("/home/softcorner/Downloads/FinalHouses_Ambedkar Nagar.kml", "r+")
    kmlstring = fo.read();
    root = parser.fromstring(kmlstring)
    data ={}                
    for number in range((root.Document.Folder.Placemark.__len__()-1)):
    	description=str(root.Document.Folder.Placemark[number].description)
    	coordinates=str(root.Document.Folder.Placemark[number].MultiGeometry.Polygon.outerBoundaryIs.LinearRing.coordinates)
    	data = {
			'description' : description ,
			'coordinates' : coordinates ,
		}
	print json.dumps(data)			


def main():
	FinalHouses_Ambedkar_Nagar()
	pass


if __name__ == "__main__":
	main()
    