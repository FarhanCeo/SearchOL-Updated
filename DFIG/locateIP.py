import geocoder
#import folium

#write a code for findind ip address location
#Geocoder API Documentation: https://geocoder.readthedocs.io/api.html

ipadd = input("Enter IP Address: ")
g = geocoder.ip(ipadd)
myaddress = g.latlng
c = g.city
s = g.state
co = g.country
print("CITY =",c)
print("STATE =",s)
print("COUNTRY =",co)
print("LatLng =",myaddress)

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
                    o.write("Location of IP: ")
                    o.write("CITY = "+str(c)+"\n")
                    o.write("STATE = "+str(s)+"\n")
                    o.write("COUNTRY = "+str(co)+"\n")
                    o.write("LatLng = "+str(myaddress)+"\n")
                    
                    
                    

                print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)
            else:
                print("File is appending to the existing file.")
                with open(filename, "a") as o:
                    o.write("RESULTS append: "+"\n")
                   ## CODE TO SAVE DATA
                    o.write("******"*5+"\n")
                    o.write("Location of IP: ")
                    o.write("CITY = "+str(c)+"\n")
                    o.write("STATE = "+str(s)+"\n")
                    o.write("COUNTRY = "+str(co)+"\n")
                    o.write("LatLng = "+str(myaddress)+"\n")
                print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)
                    
                    
        else:#when file does not exist
            with open(filename, "w") as o:
                o.write("\nRESULTS: "+"\n")
                ## CODE TO SAVE DATA
                o.write("Location of IP: ")
                o.write("CITY = "+str(c)+"\n")
                o.write("STATE = "+str(s)+"\n")
                o.write("COUNTRY = "+str(co)+"\n")
                o.write("LatLng = "+str(myaddress)+"\n")
            
                
            print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)

"""
my_map = folium.Map(location=myaddress, zoom_start=12)
folium.CircleMarker(location=myaddress,radius=50,popup="ABC").add_to(my_map)
folium.Marker(myaddress,popup="ABC").add_to(my_map)
my_map.save("my_map.html")
"""