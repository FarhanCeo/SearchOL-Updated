from fileinput import filename
filetypesdict = {
    "89504E47": "PNG",
    "25504446": "PDF",
    "FFD8": "JPG",
    "7B5C727466": "RTF",
    "D0CF11E0A1B11AE1": "MS Office",
    "526172211A70": "RAR",
    "504B34140": "DOCX, PPTX, XLSX"  
}
siglist = ["89504E47","25504446","FFD8","7B5C727466","D0CF11E0A1B11AE1","526172211A70","504B34140"]
################################################
filename = input("Enter file name: ")
f = open(filename,'rb')
bytee=0
line = ""
filecontent = f.read()
for b in filecontent:
    bytee = bytee+1
    b1 = hex(b)[2:]
    line=line+b1
    if bytee == 8:break

line1 = line.upper()
for i in range(len(filetypesdict)):
    if line1.startswith(str(siglist[i]))==True:
        filetype = filetypesdict[siglist[i]]
        print("File type is: ",filetype)
            
            
#############save the information in a file###########
import os
print("Do you want to save this in a file? (y/n)")
choice = input().capitalize()
if choice == 'Y':
    #print("Enter the file name : ")
    filename = input("Enter the file name : ").upper()
    filename = filename+'.txt'
    foldername = 'Info_Folder'
    if os.path.exists(foldername) == False:
        os.mkdir(foldername)
        os.chdir(foldername)
    else:
        os.chdir(foldername)
        if os.path.exists(filename):
            print("File already exists. Do you want to overwrite it? (y/n)")
            choice = input().capitalize()
            if choice == 'Y':
                print("File is overwriting the existing file.")
                with open(filename, "w") as o:
                    
                    o.write("\n\nRESULTS: "+"\n")
                   ## CODE TO SAVE DATA
                    o.write("File type is: "+str(filetype)+"\n")

                print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)
            else:
                print("File is appending to the existing file.")
                with open(filename, "a") as o:
                    o.write("\n\nRESULTS append: "+"\n")
                   ## CODE TO SAVE DATA
                    o.write("******"*5)
                    o.write("File type is: "+str(filetype)+"\n")
                    print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)
                    
                    
        else:#when file does not exist
            with open(filename, "w") as o:
                o.write("\nRESULTS: "+"\n")
                ## CODE TO SAVE DATA
                o.write("File type is: "+str(filetype)+"\n")
            
                
            print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)
        

############################################
"""
filename = input("Enter file name: ")
f = open(filename,'rb')
bytee=0
line = ""
filecontent = f.read()
for b in filecontent:
    bytee = bytee+1
    b1 = hex(b)[2:]
    line=line+b1
    if bytee == 8:break

print(line) 
line1 = line.upper()
print(line1)
for i in range(len(filetypesdict)):
    print("i=",i)
    print("siglist[i]=",siglist[i])
    print("line1=",line1)
    if line1.startswith(str(siglist[i]))==True:
        print("sss"*15)
        print("File type is: ",filetypesdict[siglist[i]])
        break
"""
        
"""
a = "FF D8 FF E0 0 10 4A 46"
b = "FF D8"
c = a.startswith(b)
print(c)"""
"""
from fileinput import filename

print("GGGGGG")
filename = "testexcel.xlsx"
f = open(filename,'rb')
bytee=0
line=[]
filecontent = f.read()
#print(filecontent)
for b in filecontent:
    #print("B=",b)
    bytee = bytee+1
    line.append(b)
    #print(type(b))
    print("====>{0:0{1}x}".format(b,2),end=" ")
    print("Bytee=",bytee)
    if bytee % 16 ==0:
        
        print("#",end="")
        for b2 in line:
            if (b2>=32) and (b2<=126):
                print("=>"+chr(b2),end="")
                
            else:
                print("*",end="")
        
        line=[]
        print("")    
    
    if bytee == 32:break
"""