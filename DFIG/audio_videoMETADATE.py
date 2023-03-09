# Description: This file is used to get the metadata of the audio and video files but not filetype
from tinytag import TinyTag
audio_video = input("Enter the path of the audio/video file: ")
file = TinyTag.get(audio_video)
#print(type(dict(file)))
#print(file)
album = file.album
albumartist = file.albumartist
artist = file.artist
audio_offset = file.audio_offset
bitrate = file.bitrate
channels = file.channels
comment = file.comment
composer = file.composer
disc = file.disc
disc_total = file.disc_total
duration = file.duration
extra = file.extra
filesize = file.filesize
genre = file.genre
samplerate = file.samplerate
title = file.title
track = file.track
track_total = file.track_total
year = file.year

print("album: "+str(album)+"\n"+"albumartist: "+str(albumartist)+"\n"+"artist: "+str(artist)+"\n"+"audio_offset: "+str(audio_offset)+"\n"+"bitrate: "+str(bitrate)+"\n"+"channels: "+str(channels)+"\n"+"comment: "+str(comment)+"\n"+"composer: "+str(composer)+"\n"+"disc: "+str(disc)+"\n"+"disc_total: "+str(disc_total)+"\n"+"duration: "+str(duration)+"\n"+"extra: "+str(extra)+"\n"+"filesize: "+str(filesize)+"\n"+"genre: "+str(genre)+"\n"+"samplerate: "+str(samplerate)+"\n"+"title: "+str(title)+"\n"+"track: "+str(track)+"\n"+"track_total: "+str(track_total)+"\n"+"year: "+str(year)+"\n")


##################Saving file in a text file##################
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
                    o.write("*****"*5+"\n")
                    o.write("Audio/Video Metadata:\n")
                    o.write("\n\nRESULTS: "+"\n")
                   ## CODE TO SAVE DATA
                    o.write("album: "+str(album)+"\n"+"albumartist: "+str(albumartist)+"\n"+"artist: "+str(artist)+"\n"+"audio_offset: "+str(audio_offset)+"\n"+"bitrate: "+str(bitrate)+"\n"+"channels: "+str(channels)+"\n"+"comment: "+str(comment)+"\n"+"composer: "+str(composer)+"\n"+"disc: "+str(disc)+"\n"+"disc_total: "+str(disc_total)+"\n"+"duration: "+str(duration)+"\n"+"extra: "+str(extra)+"\n"+"filesize: "+str(filesize)+"\n"+"genre: "+str(genre)+"\n"+"samplerate: "+str(samplerate)+"\n"+"title: "+str(title)+"\n"+"track: "+str(track)+"\n"+"track_total: "+str(track_total)+"\n"+"year: "+str(year)+"\n")

                print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)
            else:
                print("File is appending to the existing file.")
                with open(filename, "a") as o:
                    o.write("*****"*5+"\n")
                    o.write("Audio/Video Metadata:\n")
                    o.write("RESULTS append: "+"\n")
                   ## CODE TO SAVE DATA
                    o.write("album: "+str(album)+"\n"+"albumartist: "+str(albumartist)+"\n"+"artist: "+str(artist)+"\n"+"audio_offset: "+str(audio_offset)+"\n"+"bitrate: "+str(bitrate)+"\n"+"channels: "+str(channels)+"\n"+"comment: "+str(comment)+"\n"+"composer: "+str(composer)+"\n"+"disc: "+str(disc)+"\n"+"disc_total: "+str(disc_total)+"\n"+"duration: "+str(duration)+"\n"+"extra: "+str(extra)+"\n"+"filesize: "+str(filesize)+"\n"+"genre: "+str(genre)+"\n"+"samplerate: "+str(samplerate)+"\n"+"title: "+str(title)+"\n"+"track: "+str(track)+"\n"+"track_total: "+str(track_total)+"\n"+"year: "+str(year)+"\n")
                    print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)
                    
                    
        else:#when file does not exist
            with open(filename, "w") as o:
                o.write("\nRESULTS: "+"\n")
                o.write("Audio/Video Metadata:\n")
                ## CODE TO SAVE DATA
                o.write("album: "+str(album)+"\n"+"albumartist: "+str(albumartist)+"\n"+"artist: "+str(artist)+"\n"+"audio_offset: "+str(audio_offset)+"\n"+"bitrate: "+str(bitrate)+"\n"+"channels: "+str(channels)+"\n"+"comment: "+str(comment)+"\n"+"composer: "+str(composer)+"\n"+"disc: "+str(disc)+"\n"+"disc_total: "+str(disc_total)+"\n"+"duration: "+str(duration)+"\n"+"extra: "+str(extra)+"\n"+"filesize: "+str(filesize)+"\n"+"genre: "+str(genre)+"\n"+"samplerate: "+str(samplerate)+"\n"+"title: "+str(title)+"\n"+"track: "+str(track)+"\n"+"track_total: "+str(track_total)+"\n"+"year: "+str(year)+"\n")
            
                
            print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)





"""
a = input("Do you want to save this to a file:(y/n)")
if a.lower() == 'y':
    filename = input("Enter filename: ")
    #check if file exists in the Results folder
    print(os.path.exists("/Results/"+filename))
    print(os.getcwd())
    #list all files in the results folder
    print
    print(os.listdir())
    #print("File already exists")
"""



"""
from PIL import Image
from  PIL.ExifTags  import  TAGS
import PIL
import latlangToLocation

image = Image.open('F:\\1 SearchOL - Journel\\Code files Raw\\test.mp3')
exif = {PIL.ExifTags.TAGS[k]: v for k, v in image._getexif().items() if k in PIL.ExifTags.TAGS}
for key,value in exif.items():
    print(str(key) + " : " + str(value))  """
    
"""import mutagen
a =mutagen.File('test.mp3')
print(a)"""

