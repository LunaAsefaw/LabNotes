from datetime import datetime
import os


#create class
class PointValidator:
   
    def __init__(self):
    
        self.history=[]
        pass
    #create function that determines outcome based on option selection from user

    def options(self):
        
        options= '1. Validate point\n2. Check history\n3. Export current history\n4. Read exported file\n5. End\n'
        print(options)
        self.command= input('What would you like to do? Please only enter the number: ')
        print('selected option: ', self.command)
        
        
        if self.command=='1':
            try:
                lat=input( 'Input Latitude: ') #take input from user
                lat=float(lat)
                lon= input('Input Longtitude: ')
                lon=float(lon)
                self.validate(lat, lon)
            except ValueError:
                print('Error: Non-numeric value returned. Please input numeric value')
                self.options()#go back to input latitude step
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
            self.history=[]
            quit()
        else:
            print('Option not available. Please choose option from list below and enter only the number (1-5)')
            self.options()
            
      
    def validate(self, lat, lon):


        if lat <= 90 and lat>= -90 and lon<=180 and lon>=-180:
            print('Valid because latitude is between -90 and 90 and longtitude is between -180 and 180\n')
            reason='Valid because latitude is between -90 and 90 and longtitude is between -180 and 180'
            self.history.append([lat, lon, reason])
            self.options()
        elif lat >= 90 or lat<= -90:
            if lon<=180 and lon>=-180:
                print('Invalid because latitude should be between -90 and 90\n')
                reason= 'Invalid because latitude should be between -90 and 90'
                self.history.append([lat, lon, reason])
                self.options()
            elif lon>=180 or lon<=-180 :
                print('Invalid because latitude should be between -90 and 90 and longitude should be between -180 and 180\n')
                reason= 'Invalid because latitude should be between -90 and 90 and longitude should be between -180 and 180'
                self.history.append([lat, lon, reason])
                self.options()
        elif lon >= 180 or lon<= -180:
            if lat<=90 and lat>=-90:
                print('Invalid because longitude should be between -180 and 180\n')
                reason= 'Invalid because longitude should be between -180 and 180'
                self.history.append([lat, lon, reason])
                self.options()
    def check_history(self):
       if len(self.history)==0:
           print('You have not inputed any coordinates')
       else:
           for i in self.history:
               print(i)
       self.options()

    def export(self):
        now=datetime.now()
        date=now.strftime('%Y.%m.%d')
        time=now.strftime('%H.%M.%S')
       

        file_name='Point-'+date+'-'+time+'.txt'
        with open(file_name, 'w') as f:
           for item in self.history:
                f.write('%s\n'% item)
        print('File successfully exported :) Filename= '+ file_name +'\n')
        self.options()

    def read(self, path, option):
        self.option=option
        self.path=path
        if option==1:

            
            try:
                file=open(path, 'r')
                for line in file:
                    line=line.strip()
                    self.history.append(line)
                    length=len(file.readlines())
                length=length+1
                print('Total number of records imported: ', length)
            except FileNotFoundError:
                print("File not found. Remember to exclude inverted commas when putting file name.\n")
            self.options()

        elif option==2:
            try:
                file=open(path, 'r+')
                for line in file:
                    line=line.strip()
                    self.history.append(line)
                    length=len(file.readlines())
                length=length+1
                print('Total number of records imported: ', length)
                    
            except FileNotFoundError:
                print("File not found. Remember to exclude inverted commas when putting file path.\n")
        self.options()    
        
    def error(self):
        print('Error: Non-numeric value returned. Please input numeric value')
        self.options()

  

if __name__== '__main__':
    validator=PointValidator()
    reset=validator.options()
