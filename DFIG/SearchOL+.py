import pyfiglet
import os
print(pyfiglet.figlet_format("SearchOL", font = "slant" ,justify='center',width=100),end='A Tool For Reconnaissance')
#print(pyfiglet.figlet_format("Digital Forensic", font = "slant" ,justify='center',width=100),end='')
#print(pyfiglet.figlet_format("& ", font = "slant" ,justify='center',width=100),end='')
#print(pyfiglet.figlet_format("A Tool\n For \nReconnaissance", font = "slant" ,justify='center',width=100),end='')
print("\nDevelop By: Farhan Ahmed")
print("Version: 1F")
#print(os.getcwd())
while True:
    choice = input("Enter Your Choice: \n1:Search from Websites: \n2:Get IP address \n3:Locate the IP \n4:Server Info \n5:Port Scanning \n6:Identify File Type \n7:Image Exif Data \n8:Audio/Video Metadata \n9:Exit  \n")
    if choice == '1':
        import searchOL
    elif choice == '2':
        import getIP
    elif choice == '3':
        import locateIP
    elif choice == '4':
        import serverINFO
    elif choice == '5':
        import scanPORT
    elif choice == '6':
        import Ffiletype
    elif choice == '7':
        import imgEXIF
    elif choice == '8':
        import audio_videoMETADATE
    elif choice == '9':
        print("Thank You For Using DFIG")
        exit()    
    else:
        print("Thank You For Using DFIG")
        exit()
    
    