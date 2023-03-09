import socket
#Socket documentation: https://docs.python.org/3/library/socket.html

DomainName = input("Enter Domain Name: ")
ipadd = socket.gethostbyname(DomainName)
ghbn = socket.gethostbyname_ex(DomainName)
hostname = socket.gethostbyaddr(ipadd)
info = socket.getaddrinfo(DomainName,80)


print("IP Address of",DomainName,"is",ipadd)
print("Hostname of",ipadd,"is",hostname)
print("Info of",DomainName,"is",info)
print("ghbn of",DomainName,"is",ghbn)

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
                    o.write("\nIP Address of "+DomainName+" is "+str(ipadd))
                    o.write("\nHostname of "+ipadd+" is "+str(hostname))
                    o.write("\nInfo of "+DomainName+" is "+str(info))
                    o.write("\nghbn of "+DomainName+" is "+str(ghbn))
                    

                print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)
            else:
                print("File is appending to the existing file.")
                with open(filename, "a") as o:
                    o.write("RESULTS append: "+"\n")
                   ## CODE TO SAVE DATA
                    o.write("******"*5+"\n")
                    o.write("\nIP Address of "+DomainName+" is "+ipadd)
                    o.write("\nHostname of "+ipadd+" is "+str(hostname))
                    o.write("\nInfo of "+DomainName+" is "+str(info))
                    o.write("\nghbn of "+DomainName+" is "+str(ghbn))
                print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)
                    
                    
        else:#when file does not exist
            with open(filename, "w") as o:
                o.write("\nRESULTS: "+"\n")
                ## CODE TO SAVE DATA
                o.write("IP Address of "+DomainName+" is "+ipadd)
                o.write("Hostname of "+ipadd+" is "+str(hostname))
                o.write("Info of "+DomainName+" is "+str(info))
                o.write("ghbn of "+DomainName+" is "+str(ghbn))
            
                
            print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)
        
