import requests

url = input("Enter the URL: ")
r  = requests.get(url)
#print(r.headers)
print(r.headers['Server'])

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
                    o.write("Server Info of "+url+" is")
                    o.write(r.headers['Server'])
                    
                    
                    
                    

                print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)
            else:
                print("File is appending to the existing file.")
                with open(filename, "a") as o:
                    o.write("*****"*5+"\n")
                   ## CODE TO SAVE DATA
                    o.write("Server Info of "+url+" is")
                    o.write(r.headers['Server'])
                print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)
                    
                    
        else:#when file does not exist
            with open(filename, "w") as o:
                o.write("\nRESULTS: "+"\n")
                ## CODE TO SAVE DATA
                o.write("Server Info of "+url+" is")
                o.write(r.headers['Server'])
            
                
            print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)

