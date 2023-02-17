history=[]

def options():
    try:
        options= '1. Validate point\n2. Check history\n3. End\n'
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
            print('Goodbye')
            lat=''
            lon=''
        elif command>3 or command <1:
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
   for i in history:
       print(i)
   options()
def error():
     print('Error: Non-numeric value returned. Please input numeric value')
     options() 
     
def valid_options():
    print('Not a valid option. Select from the options below (1-3)')
    options()
options()