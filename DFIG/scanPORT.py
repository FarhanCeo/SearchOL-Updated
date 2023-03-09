import socket 
import os
#RemoteIP ='127.0.0.1' 
RemoteIP = input("Enter the IP address to scan: ")
#PortList = [20, 22, 23, 80, 135, 445, 912]

#filename = input("Enter the file name : ").upper()
filename = "Port Scan Results of "+RemoteIP+'.txt'
foldername = 'Info_Folder'
if os.path.exists(foldername) == False:
    os.mkdir(foldername)
    os.chdir(foldername)
else:
    os.chdir(foldername)
    if os.path.exists(filename):
        with open(filename, "w") as o:
            o.write("\nScan RESULTS: "+"\n")
        

query = input("Do you want to scan for all ports? (Y/N): ").upper()
if query == "Y":
    PortList = range(1,1024)
    
    for CurrentPort in PortList: 
        CurrentSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
        resultset = CurrentSocket.connect_ex((RemoteIP, CurrentPort)) 
        
        if resultset == 0: 
            print (CurrentPort,":", "Open", resultset)
            with open(filename, "a") as o:
                o.write(str(CurrentPort)+": Open "+str(resultset)+"\n")
        else:
            print(resultset)
            print (CurrentPort,":", "Closed", resultset)
            with open(filename, "a") as o:
                o.write(str(CurrentPort)+": Closed "+str(resultset)+"\n")
        #print (CurrentPort,":", resultset)
        CurrentSocket.close()
else:
    print("Enter the port numbers to scan:[1 2 3 4 5] ")
    try:
        PortList = [int(x) for x in input().split()]
    except ValueError:
        print("Please enter numbers only.")
     
    for CurrentPort in PortList:
        CurrentSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
        resultset = CurrentSocket.connect_ex((RemoteIP, CurrentPort)) 
        if resultset == 0: 
            print (CurrentPort,":", "Open", resultset)
            with open(filename, "a") as o:
                o.write(str(CurrentPort)+": Open "+str(resultset)+"\n")
        else:
            print (CurrentPort,":", "Closed", resultset)
            with open(filename, "a") as o:
                o.write(str(CurrentPort)+": Closed "+str(resultset)+"\n")
        #print (CurrentPort,":", resultset)
        CurrentSocket.close()
        
        

