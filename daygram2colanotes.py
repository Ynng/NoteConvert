import json
from datetime import datetime
import os

inputdirectory = input(
    "Enter the path of the daygram export file, for examples C:\\Users\\bob\\Documents\\January 1 Monday 2019.txt\n").strip("\"")
if (not os.path.exists(inputdirectory)) or(not os.path.isfile(inputdirectory)):
    print("The file, \""+str(inputdirectory)+"\" Does not exist\n")
    exit()
inputfile = open(inputdirectory,encoding="utf-8")
print("We found your file!\n")

outputdirectory = inputdirectory.split("\\")
outputdirectory.pop(len(outputdirectory)-1)
outputdirectory = "\\".join(outputdirectory)
outputfile = open(outputdirectory+'\com.colanotes.android.entity.NoteEntity', 'w',encoding="utf-8")


def write_note(note):
    if(bool(note)):
        note["text"] = note["text"].strip("\n")
        outputfile.write(json.dumps(note)+"\n")
    return


note = {}
for line in inputfile:
    # line=line.rstrip('\n')
    if(line.startswith("**") and line.endswith("**\n")):
        write_note(note)
        note.clear()
        date = datetime.strptime(line.lstrip(
            "** ").rstrip(" **\n"), "%B %d %A %Y")
        note["creationDate"] = note["modificationDate"] = int(
            date.timestamp())*1000
        # note["creationDate"]=note["modificationDate"]=note["id"]=int(date.timestamp())*1000
        # note["pinned"]=False
        # note["typography"]=1
        # note["styles"]=[0,0,0,0]
        # note["state"]=note["type"]=0
        # note["images"]=""
        note["text"] = ""
    else:
        note["text"] = note["text"]+line
write_note(note)
inputfile.close()
outputfile.close()
input("\nFinished, file placed at\""+outputdirectory+"\\com.colanotes.android.entity.NoteEntity\",\n Please place the file under the root directory of a zip file for import in Cola Note\nPress Enter to continue...")
    
