import requests
import os   
import pyfiglet
from bs4 import BeautifulSoup

#print(pyfiglet.figlet_format("SearchOL", font = "slant" ,justify='center',width=100),end='')
#print("Develop By: Farhan Ahmed")
#print("Version: 1F")

key = input("ENTER THE KEYWORD TO SEARCH: ")
key2 = key.replace(" ","+")
urlG = 'https://www.google.co.in/search?q=allintitle:'+key2
urlB = 'https://www.bing.com/search?q='+key2
urlA = 'https://www.ask.com/web?q='+key2
urlY = 'https://in.search.yahoo.com/search?q='+key2

sitelist=[]
links = []
c =0
Ukey = key.upper()
Lkey = key.lower()
Tkey = key.title()
print("SEARCHING FOR: ",key)
for url in [urlB,urlG,urlA,urlY]:
    r = requests.get(url)
    if url == urlB:
        print("SEARCHING IN BING")
    elif url == urlG:
        print("SEARCHING IN GOOGLE")
    elif url == urlA:
        print("SEARCHING IN ASK")
    elif url == urlY:
        print("SEARCHING IN YAHOO")
    print()
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    title = soup.title   
    anchor = soup.find_all('a')
    for link in anchor:
        hl = link.get('href')
        if hl!=None:
            if Ukey or Lkey or Tkey in hl:
                if url == urlG:
                    if hl.startswith('/url?q=https://www.') or hl.startswith('/url?q=https://en.') or hl.startswith('/url?q=https://in.') or hl.startswith('/url?q=https://twitter.') :
                        #print(hl)
                        fhl = url[:24]+hl
                        i = fhl.index('&')
                        j = fhl.index('?q=')
                        fhl2 = fhl[:i]
                        fhl1 = fhl[j+3:i]
                        txt = fhl[39:]
                        if '.com' in txt:
                            a = txt.index('com')
                            txt1 = txt[:a+3]
                            if txt1 not in sitelist:
                                sitelist.append(txt1)
                        elif '.org' in txt:
                            a = txt.index('org')
                            txt1 = txt[:a+3]
                            if txt1 not in sitelist:
                                sitelist.append(txt1)
                                
                        if 'youtube' in fhl:
                            if fhl2 not in links:
                                #print("fhl2: ",fhl2)
                                links.append(fhl2)
                            
                        elif 'instagram' in fhl:
                            if '%3' in fhl1:
                                k = fhl.index('%3')
                                fhl3 = fhl[j+3:k]
                            
                            if fhl3 not in links:
                                #print("fhl3: ",fhl3)
                                links.append(fhl3)

                        else:
                            if fhl1 not in links:
                                #print("fhl1: ",fhl1)
                                links.append(fhl1)
                    

                elif url == urlB:
                    if hl.startswith('https://www.') or hl.startswith('https://en.') or hl.startswith('https://in.') or hl.startswith('https://twitter.') :
                        if hl not in links:
                            links.append(hl)                          
                    
                elif url == urlA:
                    if (hl.startswith('https://www.ask')==False) and (hl.startswith('https://help')==False)  and (hl.startswith('https://') or hl.startswith('https://www.') or hl.startswith('https://en.') or hl.startswith('https://in.') or hl.startswith('https://twitter.')) :
                        if hl not in links:
                            links.append(hl)
                            
                elif url == urlY:
                    if (hl.startswith('https://in.help.')==False) and(hl.startswith('https://in.mail.')==False) and(hl.startswith('https://in.video.')==False) and(hl.startswith('https://in.search.')==False) and(hl.startswith('https://in.images.search.')==False) and (hl.startswith('https://www.') or hl.startswith('https://en.') or hl.startswith('https://in.') or hl.startswith('https://twitter.')) :    
                        if hl not in links:
                            links.append(hl)
                        
                              
for link in links:
    if '.com' in link:
        a = link.index('com')
        txt1 = link[8:a+3]
        if txt1 not in sitelist:
            sitelist.append(txt1)
        elif '.org' in link:
            a = link.index('org')
            txt1 = link[8:a+3]
            if txt1 not in sitelist:
                sitelist.append(txt1)                               

##PRINT INFO
print("Total sites => ",len(sitelist))
for i in sitelist:
    print("siteName = ",i)
c=0
print("len of links=",len(links))
for j in links:
    c+=1
    print("["+str(c)+"]"+"=>"+j)
    
##SAVE INFO

print("Do you want to save the links in a file? (y/n)")
choice = input().capitalize()
if choice == 'Y':
    print("Enter the file name to save the links: ")
    filename = input().upper()
    filename = filename+'.txt'
    foldername = 'Info_Folder'
    #print(os.getcwd())
    if os.path.exists(foldername) == False:
        os.mkdir(foldername)
        os.chdir(foldername)
        with open(filename, "w") as o:
            o.write("SEARCH RESULT FOR: "+key+"\n")
            o.write("Total links => "+str(c)+"\n")
            o.write("Total sites => "+str(len(sitelist))+"\n")
            o.write("\nSITE LINKS:\n")
            for i in links:
                o.write("[+]:"+i+"\n")

        with open(filename, "a") as o:
            o.write("#"*50+"\n\n")
            o.write("\nSITE LIST:\n")
            for i in sitelist:
                o.write("[+]:"+i+"\n")
        print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)
        print(os.getcwd())
    else:
        os.chdir(foldername)
        print(os.getcwd())
        if os.path.exists(filename):
            print("File already exists. Do you want to overwrite it? (y/n)")
            choice = input().capitalize()
            if choice == 'Y':
                with open(filename, "w") as o:
                    o.write("SEARCH RESULT FOR: "+key+"\n")
                    o.write("Total links => "+str(c)+"\n")
                    o.write("Total sites => "+str(len(sitelist))+"\n")
                    o.write("\nSITE LINKS:\n")
                    for i in links:
                        o.write("[+]:"+i+"\n")

                with open(filename, "a") as o:
                    o.write("#"*50+"\n\n")
                    o.write("\nSITE LIST:\n")
                    for i in sitelist:
                        o.write("[+]:"+i+"\n")
                print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)
            
            else:
                with open(filename, "a") as o:
                    o.write("******"*5)
                    o.write("SEARCH RESULT FOR: "+key+"\n")
                    o.write("Total links => "+str(c)+"\n")
                    o.write("Total sites => "+str(len(sitelist))+"\n")
                    o.write("\nSITE LINKS:\n")
                    for i in links:
                        o.write("[+]:"+i+"\n")

                with open(filename, "a") as o:
                    o.write("#"*50+"\n\n")
                    o.write("\nSITE LIST:\n")
                    for i in sitelist:
                        o.write("[+]:"+i+"\n")
                    
                    
        else:
            #os.chdir(foldername)
            print(os.getcwd())
            with open(filename, "w") as o:
                o.write("SEARCH RESULT FOR: "+key+"\n")
                o.write("Total links => "+str(c)+"\n")
                o.write("Total sites => "+str(len(sitelist))+"\n")
                o.write("\nSITE LINKS:\n")
                for i in links:
                    o.write("[+]:"+i+"\n")

            with open(filename, "a") as o:
                o.write("#"*50+"\n\n")
                o.write("\nSITE LIST:\n")
                for i in sitelist:
                    o.write("[+]:"+i+"\n")
                
            print("File saved successfully! in folder \""+foldername + "\" with filename: "+filename)

##END
