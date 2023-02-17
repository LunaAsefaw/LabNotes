from datetime import datetime
import os
#global variable
history=[]

#create class
class Validator:
   
    def __init__(self, command):
        self.command=command
    #create function that determines outcome based on option selection from user
    def options(self, history):
        
        
        if self.command=='1':
            try:
                lat=input( 'Input Latitude: ') #take input from user
                lat=float(lat)
                lon= input('Input Longtitude: ')
                lon=float(lon)
                self.validate(lat, lon, history)
            except ValueError:
                
                print('Error: Non-numeric value returned. Please input numeric value')
                self.options(history)#go back to input latitude step
        elif self.command=='2':
            self.check_history()
            
        elif self.command=='3':
            self.export()

        elif self.command=='4':
            print('Would you like to input file name or file path? \nNB Use file name only if the file is in the same location as the python file\n')
            try:
                option=int(input('Enter 1 for file name or 2 for file path: '))
                path=input('Enter file name/file path (without inverted commas): ')
                self.read(path, option)
            except ValueError:
                error()
            
        elif self.command=='5':
            print('Goodbye')
            history=[]
            quit()
        else:
            print('Option not available. Please choose option from list below and enter only the number (1-5)')
            reset()
            
            
    def validate(self, lat, lon, history):
        self.lat=lat
        self.lon=lon

        if lat <= 90 and lat>= -90 and lon<=180 and lon>=-180:
            print('Valid because latitude is between -90 and 90 and longtitude is between -180 and 180\n')
            reason='Valid because latitude is between -90 and 90 and longtitude is between -180 and 180'
            history.append([lat, lon, reason])
            reset()
        elif lat >= 90 or lat<= -90:
            if lon<=180 and lon>=-180:
                print('Invalid because latitude should be between -90 and 90\n')
                reason= 'Invalid because latitude should be between -90 and 90'
                history.append([lat, lon, reason])
                reset()
            elif lon>=180 or lon<=-180 :
                print('Invalid because latitude should be between -90 and 90 and longitude should be between -180 and 180\n')
                reason= 'Invalid because latitude should be between -90 and 90 and longitude should be between -180 and 180'
                self.history.append([lat, lon, reason])
                reset()
        elif lon >= 180 or lon<= -180:
            if lat<=90 and lat>=-90:
                print('Invalid because longitude should be between -180 and 180\n')
                reason= 'Invalid because longitude should be between -180 and 180'
                history.append([lat, lon, reason])
                reset()
    def check_history(self):
       if len(history)==0:
           print('You have not inputed any coordinates')
       else:
           for i in history:
               print(i)
       reset()

    def export(self):
        d=datetime.now()
        only_date, only_time= d.date(), d.time()
        date= str(only_date)
        time=str(only_time)
       
        name_1=date[0:4]+ '.'+ date[5:7]+'.'+date[9:]
        name_2=time[0:2]+'.'+time[3:5]+'.'+time[6:8]
        file_name='Point-'+name_1+'-'+name_2+'.txt'
        with open(file_name, 'w') as f:
           for item in history:
                f.write('%s\n'% item)
        print('File successfully exported :) Filename= '+ file_name +'\n')
        reset()

    def read(self, path, option):
        self.option=option
        self.path=path
        if option==1:

            
            try:
                file=open(path, 'r')
                for line in file:
                    line=line.strip()
                    history.append(line)
                    print(history)
            except FileNotFoundError:
                print("File not found. Remember to exclude inverted commas when putting file name.\n")
            reset()

        elif option==2:
            try:
                file=open(path, 'r+')
                for line in file:
                    line=line.strip()
                    history.append(line)
                    print(history)
            except FileNotFoundError:
                print("File not found. Remember to exclude inverted commas when putting file path.\n")
        reset()    
        
    def error(self):
        print('Error: Non-numeric value returned. Please input numeric value')
        reset() 

        
def reset():
    options= '1. Validate point\n2. Check history\n3. Export current history\n4. Read exported file\n5. End\n'
    print(options)
    command= input('What would you like to do? Please only enter the number: ')
    print('selected option: ', command)
  
    test=Validator(command) #object
    test.options(history)
reset() 
