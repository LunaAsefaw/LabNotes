from datetime import datetime
import os
history=[]

def options():
    
    try:
        options= '1. Validate point\n2. Check history\n3. Export current history\n4. Read exported file\n5. End\n'
        print(options)
        command= input('What would you like to do? Please only enter the number: ')
        print('selected option: ', command)
        command= int(command)
        
        if command==1:
    
            try:
                lat=input( 'Input Latitude: ')
                lat=float(lat)
                lon= input('Input Longtitude: ')
                lon=float(lon)
                validate(lat, lon)
            except ValueError:
                error()
                
                
            
        elif command==2:
            check_history(history)
         
            
        elif command==3:
            export(history)

        elif command==4:
            print('Would you like to input file name or file path? \nNB Use file name only if the file is in the same location as the python file\n')

            try:
                options=int(input('Enter 1 for file name or 2 for file path: '))
                path=input('Enter file name/file path (without inverted commas): ')
                
                read(options, path)
            except ValueError:
                error()
            
            

        elif command==5:
            
            print('Goodbye')
            quit()
            #lat=''
            #lon=''
            #history=[]
        elif command>5 or command <1:
            valid_options()
        
    except ValueError:
        error()

def validate(lat, lon):
    if lat <= 90 and lat>= -90 and lon<=180 and lon>=-180:
        print('Valid because latitude is between -90 and 90 and longtitude is between -180 and 180\n')
        reason='Valid because latitude is between -90 and 90 and longtitude is between -180 and 180'
        history.append([lat, lon, reason])
        
        options()


    elif lat >= 90 or lat<= -90:
        if lon<=180 and lon>=-180:
            print('Invalid because latitude should be between -90 and 90\n')
            reason= 'Invalid because latitude should be between -90 and 90'
            history.append([lat, lon, reason])
            options()
        elif lon>=180 or lon<=-180 :
            print('Invalid because latitude should be between -90 and 90 and longitude should be between -180 and 180\n')
            reason= 'Invalid because latitude should be between -90 and 90 and longitude should be between -180 and 180'
            history.append([lat, lon, reason])
            options()
            
    elif lon >= 180 or lon<= -180:
        if lat<=90 and lat>=-90:
            print('Invalid because longitude should be between -180 and 180\n')
            reason= 'Invalid because longitude should be between -180 and 180'
            history.append([lat, lon, reason])
            options()
            



def check_history(history):
   # history.append([lat, lon])
   if len(history)==0:
       print('You have not inputed any coordinates')
   else:
       for i in history:
           print(i)
   options()
def export(history):
   d=datetime.now()
   only_date, only_time= d.date(), d.time()
   date= str(only_date)
   time=str(only_time)
   
   name_1=date[0:4]+ '.'+ date[5:7]+'.'+date[9:]
   name_2=time[0:2]+'.'+time[3:5]+'.'+time[6:8]
   file_name=name_1+'-'+name_2+'.txt'
   with open(file_name, 'w') as f:
       for item in history:
           f.write('%s\n'% item)
   print('File successfully exported :) Filename= '+ file_name +'\n')
   options()
def read(input, path):
    if input==1:

        #file=open(path, 'r')
        try:
            file=open(path, 'r')
            for line in file:
                line=line.strip()
                history.append(line)
                print(history)
        except FileNotFoundError:
            print("File not found. Remember to exclude inverted commas when putting file name.\n")


    elif input==2:
        try:
            file=open(path, 'r+')
            for line in file:
                line=line.strip()
                history.append(line)
                print(history)
        except FileNotFoundError:
            print("File not found. Remember to exclude inverted commas when putting file path.\n")
    options()
def error():
     print('Error: Non-numeric value returned. Please input numeric value')
     options() 
     
def valid_options():
    print('Not a valid option. Select from the options below (1-5)')
    options()
options()
