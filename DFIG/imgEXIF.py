from PIL import Image
from  PIL.ExifTags  import  TAGS
import PIL
import latlangToLocation

img = input("Enter the image name with extension or image path: ")
image = Image.open(img)
location = ""

try:
    exif = {PIL.ExifTags.TAGS[k]: v for k, v in image._getexif().items() if k in PIL.ExifTags.TAGS}
    flag = 1
    if 'GPSInfo' in exif:
        north = exif['GPSInfo'][2]
        east = exif['GPSInfo'][4]
        #print(north)
        #print(east)
        lat = float(((((north[0]*60) + north[1])*60) + north[2])/60/60)
        lang = float(((((east[0]*60) + east[1])*60) + east[2])/60/60)
        #print(lat)
        #print(lang)


        location = latlangToLocation.get_location_name(str(lat), str(lang))
        print(location)
        poplist = ['ExifImageHeight','ExposureMode','WhiteBalance','MakerNote','GPSInfo', 'ExifImageWidth']
        for i in poplist:
            exif.pop(i)
        for key,value in exif.items():
            print(str(key) + " : " + str(value))  
    else:
        print("No GPS data found")
except:
    flag = 0
    location = "No EXIF data found"
    print("No EXIF data found")

    


#gps = get_gps(image)  

#print(gps)
    
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
                    o.write("Image Exif Data:")
                   ## CODE TO SAVE DATA
                    
                    o.write("Location: "+str(location))
                    if flag == 1:
                        for key,value in exif.items():
                            o.write("\n"+str(key) + " : " + str(value))  
                    

                print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)
            else:
                print("File is appending to the existing file.")
                with open(filename, "a") as o:
                    #o.write("RESULTS append: "+"\n")
                   ## CODE TO SAVE DATA
                    o.write("******"*5+"\n")
                    o.write("Image Exif Data:")
                    o.write("Location: "+str(location))
                    if flag ==1:
                        for key,value in exif.items():
                            o.write("\n"+str(key) + " : " + str(value)) 
                print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)
                    
                    
        else:#when file does not exist
            with open(filename, "w") as o:
                o.write("\nRESULTS: "+"\n")
                o.write("Image Exif Data:")
                ## CODE TO SAVE DATA
                o.write("Location: "+str(location))
                if flag == 1:
                    for key,value in exif.items():
                        o.write("\n"+str(key) + " : " + str(value)) 
            
                
            print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)
        




"""
pillow_img = Image.open('F:\\1 SearchOL - Jo
urnel\\Code files Raw\\c.jpg')
exifdata = pillow_img._getexif()

imgExif = exifdata.items()

for tagid in exifdata:
     
    # getting the tag name instead of tag id
    tagname = TAGS.get(tagid, tagid)

    # passing the tagid to get its respective value
    value = exifdata.get(tagid)
   
    # printing the final result
    print(f"{tagname:25}: {value}")"""