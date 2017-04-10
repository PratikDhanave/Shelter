from pykml import parser
import json
from BeautifulSoup import BeautifulSoup

"""
def FinalHouses_Ambedkar_Nagar():
    fo = open("/home/softcorner/Downloads/FinalHouses_Ambedkar Nagar.kml", "r+")
    kmlstring = fo.read();
    root = parser.fromstring(kmlstring)
    data ={}
    FinalHouses_Ambedkar_NagarArray = []
    count = 0
    for number in range(root.Document.Folder.Placemark.__len__()):
        description = ""
        description=str(root.Document.Folder.Placemark[number].description)
        soup = BeautifulSoup(description)
        try:
            soup.find(text="slumname").replaceWith("Slum name")
        except:
            pass
        try:
            soup.find(text="FinalStatu").replaceWith("Final status")
        except:
            pass
        try:
            soup.find(text="MobileNumb").replaceWith("Mobile number")
        except:
            pass
        try:
            soup.find(text="WasteColle").replaceWith("Waste collection")
        except:
            pass
        try:
            soup.find(text="WaterConne").replaceWith("Water collection")
        except:
            pass
        try:
            soup.find(text="Nooffamily").replaceWith("No of family Member")
        except:
            pass
        try:
            soup.find(text="Nooffamily").replaceWith("No of family Member")
        except:
            pass
        try:
            soup.find(text="HouseStruc").replaceWith("House structure")
        except:
            pass
        try:
            soup.find(text="NewRHSNo").replaceWith("New RHS No")
        except:
            pass
        try:
            soup.find(text="toiletisco").replaceWith("Is toilet connected")
        except:
            pass
        try:
            soup.find(text="Currentpla").replaceWith("Current place defecation")
        except:
            pass
        try:
            soup.find(text="HouseAreaC").replaceWith("House area")
        except:
            pass
        try:
            soup.find(text="HouseOwner").replaceWith("Owenship status")
        except:
            pass
        try:
            soup.find(text="HouseOccup").replaceWith("House occupancy")
        except:
            pass
        try:
            soup.find(text="householdc").replaceWith("Household Code")
        except:
            pass
        try:
            soup.find(text="NewRHSNo").replaceWith("New RHS No")
        except:
            pass
        try:
            soup.find(text="Ifyeshowma").replaceWith("If yes how many ?")
        except:
            pass
        try:
            soup.find(text="Doyouhaveg").replaceWith("Do you have girl child ?")
        except:
            pass
        try:
            soup.find(text="Typeoftoil").replaceWith("Type of material for toilet")
        except:
            pass
        try:
            soup.find(text="Interested").replaceWith(" Interested in Household toilet")
        except:
            pass
        description=str(soup)
        string=str(root.Document.Folder.Placemark[number].MultiGeometry.Polygon.outerBoundaryIs.LinearRing.coordinates)
    	coordinates=string.replace("\t","").replace("\n","")
        data = { 'description'  : description,
    			 'coordinates': coordinates
    			}
        FinalHouses_Ambedkar_NagarArray.append(data)
        count = count + 1
    val = { 'FinalHouses_Ambedkar_NagarArray'  : FinalHouses_Ambedkar_NagarArray}
    jsondata=json.dumps(val)
    print jsondata
    print "\n\n"
    print count
    fo = open("FinalHouses_Ambedkar_Nagar_HTML.json", "ab")
    fo.write(jsondata)
    fo.close
"""
def Final_Current_Place_of_Dececation_Ambedkar_Nagar():
    fo = open("/home/softcorner/Downloads/Final Current Place of Dececation_Ambedkar Nagar.kml", "r+")
    kmlstring = fo.read();
    root = parser.fromstring(kmlstring)
    data ={}
    Final_Current_Place_of_Dececation_Ambedkar_NagarArray = []
    count = 0
    pdfcout = 0
    for i in range(root.Document.Folder.__len__()):
        for j in range(root.Document.Folder[i].Placemark.__len__()):
            try:
                coordinates = ""
                coordinates=str(root.Document.Folder[i].Placemark[j].LineString.coordinates)
                name=str(root.Document.Folder[i].Placemark[j].name)
                styleUrl=str(root.Document.Folder[i].Placemark[j].styleUrl)
                typeof = "Line"
                count = count + 1
                data = { 'name'  : name,
            			 'coordinates': coordinates,
                         'styleUrl' : styleUrl,
                         'typeof': typeof

                         }
                Final_Current_Place_of_Dececation_Ambedkar_NagarArray.append(data)
            except:
                coordinates = ""
                coordinates=str(root.Document.Folder[i].Placemark[j].Polygon.outerBoundaryIs.LinearRing.coordinates)
                name=str(root.Document.Folder[i].Placemark[j].name)
                styleUrl=str(root.Document.Folder[i].Placemark[j].styleUrl)
                typeof = "Polygon"
                if styleUrl=="#Style9":
                    pdffile = name.split(")")[1] + "_Ambedkar Nagar_Bibvewadi_Pune_2016.pdf"
                    fo = open("/media/softcorner/DATA/ambedkar Nagar/file.txt", "r+")
                    pdffilenames  = fo.read()
                    arrayname = pdffilenames.split("\n")
                    if pdffile in arrayname:
                        pdfcout = pdfcout + 1
                        print pdffile
                    data = { 'name'  : name,
                			 'coordinates': coordinates,
                             'styleUrl' : styleUrl,
                             'typeof': typeof,
                             'pdf'   : pdffile
                             }
                else:
                    data = { 'name'  : name,
                			 'coordinates': coordinates,
                             'styleUrl' : styleUrl,
                             'typeof': typeof
                             }
                Final_Current_Place_of_Dececation_Ambedkar_NagarArray.append(data)
                count = count + 1
                pass
    data = {'Final_Current_Place_of_Dececation_Ambedkar_NagarArray': Final_Current_Place_of_Dececation_Ambedkar_NagarArray}
    jsondata=json.dumps(data)
    print count
    print pdfcout
    fo = open("Final_Current_Place_of_Dececation_Ambedkar_Nagar.json", "ab")
    fo.write(jsondata)
    fo.close



def FinalHouses_Ambedkar_Nagar():
    fo = open("/home/softcorner/Downloads/Dec8Houses.kml", "r+")
    kmlstring = fo.read();
    root = parser.fromstring(kmlstring)
    data ={}
    FinalHouses_Ambedkar_NagarArray = []
    count = 0
    for number in range(root.Document.Folder.Placemark.__len__()):
        description = ""
        description=str(root.Document.Folder.Placemark[number].description)
        soup = BeautifulSoup(description)
        try:
            soup.find(text="slumname").replaceWith("Slum name")
        except:
            pass
        try:
            soup.find(text="FinalStatu").replaceWith("Final status")
        except:
            pass
        try:
            soup.find(text="MobileNumb").replaceWith("Mobile number")
        except:
            pass
        try:
            soup.find(text="WasteColle").replaceWith("Waste collection")
        except:
            pass
        try:
            soup.find(text="WaterConne").replaceWith("Water collection")
        except:
            pass
        try:
            soup.find(text="Nooffamily").replaceWith("No of family Member")
        except:
            pass
        try:
            soup.find(text="HouseStruc").replaceWith("House structure")
        except:
            pass
        try:
            soup.find(text="NewRHSNo").replaceWith("New RHS No")
        except:
            pass
        try:
            soup.find(text="toiletisco").replaceWith("Is toilet connected")
        except:
            pass
        try:
            soup.find(text="Currentpla").replaceWith("Current place defecation")
        except:
            pass
        try:
            soup.find(text="HouseAreaC").replaceWith("House area")
        except:
            pass
        try:
            soup.find(text="HouseOwner").replaceWith("Owenship status")
        except:
            pass
        try:
            soup.find(text="HouseOccup").replaceWith("House occupancy")
        except:
            pass
        try:
            soup.find(text="householdc").replaceWith("Household Code")
        except:
            pass
        try:
            soup.find(text="Ifyeshowma").replaceWith("If yes how many ?")
        except:
            pass
        try:
            soup.find(text="Doyouhaveg").replaceWith("Do you have girl child ?")
        except:
            pass
        try:
            soup.find(text="Typeoftoil").replaceWith("Type of material for toilet")
        except:
            pass
        try:
            soup.find(text="Interested").replaceWith(" Interested in Household toilet")
        except:
            pass
        description=str(soup)
        string=str(root.Document.Folder.Placemark[number].MultiGeometry.Polygon.outerBoundaryIs.LinearRing.coordinates)
    	coordinates=string.replace("\t","").replace("\n","")
        data = { 'description'  : description,
    			 'coordinates': coordinates
    			}
        FinalHouses_Ambedkar_NagarArray.append(data)
        count = count + 1
    val = { 'FinalHouses_Ambedkar_NagarArray'  : FinalHouses_Ambedkar_NagarArray}
    jsondata=json.dumps(val)
    print jsondata
    print "\n\n"
    print count
    fo = open("Dec8Houses.json", "ab")
    fo.write(jsondata)
    fo.close





def main():
    Final_Current_Place_of_Dececation_Ambedkar_Nagar()#FinalHouses_Ambedkar_Nagar()#
    pass

if __name__ == "__main__":
	main()
