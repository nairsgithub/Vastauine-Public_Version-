#!/usr/bin/env/python
#updated 06/06/2016
#(update)This is VastauineIOT Project's PYTHON_SQL_PHP PYTHON END SOFTWARE.VERSION 1.0
#This Version adds support for all users Registred at vastauine.com
#This Version reduces CPU usage
#(update)This version adds support to reconnect Itself Support 2.1
#NEED FOR MODIFICATION FOR INCORRECT USERNAME
print("Vastauine IOT Windows.v.1")
print("Use ctrl + C to Terminate")

#IMPORTING Necessary components
import time
from datetime import datetime
import MySQLdb
import os
import urllib2 as url

#Function to turn pin's ON or OFF

def internet_Status():
    try:
        time.sleep(0.01)
        response=url.urlopen('http://111.118.215.65',timeout=1)
        return 1
    except:
        print("INTERNET DISCONNECTED")
	internet_Status();    
    

def piON(pin,state):
        
    import RPi.GPIO as GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,True)
    #print "ON",pin,state;

def piOFF(pin,state):
        
    import RPi.GPIO as GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,False)
    #print "OFF",pin,state;

################################################################

def main(entred_username,entred_password):

    print("We Made IT")
    #MYSQL_Making connection to rpi database
    try:
        #Contact Vastauine at care@vastauine.com For Details Regarding Database Password.
    	conn1=MySQLdb.connect(user='#####',passwd='#######',host='111.118.215.65',db='######')
    except:
        print("Main Function Got an Exception Connecting to Pin Database")
	main(entred_username,entred_password)
    else:
	mycursor=conn1.cursor()
    

    #MYSQL_Making connection to rpi database
    try:
    	conn2=MySQLdb.connect(user='#####',passwd='#####',host='111.118.215.65',db='#####')
    except:
        print("MAIN FUNCTION GOT EXCEPTION Connecting To UserDatabase")
	main(entred_username,entred_password)
    else:
    	authentication_cursor=conn2.cursor()

    print("Sucessfully connected to server")
    
    #MYSQL DATABASE USERNAME PASSWORD AUTHENTICATION
    var1=entred_username;
    authentication_cursor.execute("""SELECT userpassword
                         FROM userinfo
                         WHERE username=('%s')"""%(var1))
    Dictionary=(authentication_cursor.fetchall())

    unpackDictionary=Dictionary[0]
    user_password=unpackDictionary[0]



    if entred_password==user_password :
        os.system('clear')
        print ("Welcome ",entred_username," You are Logged In ")
        print ("You can now start using devices By going to www.vastauine.com/iot")
        
        #LOOP To Fetch Data 

        #key=2
        while(internet_Status()==1):    
            try: 
                mycursor.execute("""SELECT gpio01,gpio02,gpio03,gpio04,gpio05,gpio06,gpio07,gpio08,gpio09,gpio10,gpio11,gpio12,gpio13,gpio14,
                                       gpio15,gpio16,gpio17,gpio18,gpio19,gpio20,gpio21,gpio22,gpio23,gpio24,gpio25,gpio26,gpio27
                             FROM pi
                             WHERE username=('%s')"""%(var1))
            except:
                print("Got Exception While Fetching Data From Database")
                main(entred_username,entred_password)
            else:
                var=(mycursor.fetchall())
            i=0;
            #"This line selects first array from associative array [()] => ()"
            xvar=var[i];
            while (i<1):
                #"This For loop pin is the Index of J  and J is values from array retrived in above step" 
                for pin, j in enumerate(xvar):
                        if j == 1:
                            state=1
                            print (str(datetime.now()))
                            piON(pin+1,state)
                        elif j == 0:
                            state=0
                            piOFF(pin+1,state)
                        else:
                            print ("We Encountred some ERROR INCORRECT DATABASE ERROR ")
                            exit(errorExit);          
                        
                        i=i+1;
                time.sleep(0.01)
               
                #key=key+1;
                #while(i == 1  or i>1):
		#print ("this error")
		#i=i+1
		
            while(internet_Status()!=1):
                print("Trying To Reconnect ...")
                main(entred_username,entred_password)
    else:
	print("You Entred an Incorrect Password")
        exit(Errorexit)            

####################################################################################################

print("------------------------------------")

entred_username = str(raw_input('Enter User Name : '))
entred_password =str(raw_input('Enter Password : '))

#USE THIS WHEN USING  PYTHON 3
#entred_username = str(input('Enter User Name : '))
#entred_password =str(input('Enter Password : '))

print("------------------------------------")
while(True):
	main(entred_username,entred_password)
print("Program complete")
             
        
         
           
    

