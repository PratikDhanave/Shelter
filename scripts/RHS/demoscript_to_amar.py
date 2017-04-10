import os
import requests
from multiprocessing import Pool

folder="/home/softcorner/ShelterAssociates/src/scripts/RHS/xmlfiles/RHS_parag/RHS_288_shelter/slum_288/"#"/home/softcorner/ShelterAssociates/src/scripts/RHS/xmlfiles/Family Mumbai/FF_shelter_45_288/slum_288"
count=0

xml_files=[]

def searchfile():
    for filename in os.listdir(folder):
        if filename.endswith(".xml"):
	    print filename
	    xml_files.append(filename)


def sentfile(file_name):
    global count
    print str(count)
    mypath = str(folder) + str(file_name)
    filepath=open(mypath,"rb")
    objresponse=requests.post("http://192.168.0.87:8001/api/v1/submissions", auth=("amar","softcorner"), files={"xml_submission_file": filepath})
    count += 1
    fp=open(str(objresponse.status_code), 'ab')
    fp.write("\nResponse : "+str(file_name)+" ----  "+ str(objresponse.text))
    fp.close()
    return objresponse

def main():
    searchfile()
    print len(xml_files)
    print xml_files
    objpool=Pool(7)
    result=objpool.map(sentfile,xml_files)
    objpool.close()
    objpool.join()

if __name__=="__main__":
    main()
