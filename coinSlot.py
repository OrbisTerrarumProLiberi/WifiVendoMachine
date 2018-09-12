#!/usr/bin/python

print ("Awaiting Coin")
import pymysql.cursors
import os
import string
from random import *
import time
import Adafruit_CharLCD as LCD
import  RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(2, GPIO.IN,pull_up_down=GPIO.PUD_UP)
lcd_rs        = 7 
lcd_en        = 8
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 4
lcd_columns = 16
lcd_rows    = 2


lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,lcd_columns, lcd_rows, lcd_backlight)
lcd.message("AWAITING COIN")

try:
    while True:
	    inputValue = GPIO.input(2)
	    if (inputValue == False):
		    sqlconn = pymysql.connect(user='radius',
                    password='radpass',
                    host='localhost',
                    database='radius',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor)
			
		    min_char = 5
		    max_char = 5
		    allchar = string.ascii_uppercase + string.digits
		    password = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
		    print ("Your Code is:\n", password)	
		    break
			
finally:
    try:    			
	    with sqlconn.cursor() as cursor:
                sql = ("INSERT INTO `radcheck` (`username`,`attribute`,`op`,`value`) VALUES (%s,'Auth-Type',':=','Accept')",(password))
                cursor.execute(*sql)
                sql = ("INSERT INTO `radreply` (`username`,`attribute`,`op`,`value`) VALUES (%s,'Session-Timeout',':=','3600')",(password))
                cursor.execute(*sql)
                sqlconn.commit()    
    finally:
         
        print("Connection Established")
        lcd.clear()
lcd.message("Your Code:\n" + str(password))
############################################################################################################
try:
    while True:
        with sqlconn.cursor() as cursor:
             sql = ("SELECT * FROM `radacct` WHERE username = '%s'" % (password))
             cursor.execute(sql)
             result = cursor.execute(sql)
             sqlconn.commit()
             #print(result)
             time.sleep(1)
             actionRevoke = GPIO.input(26)
        if(result > 0 or actionRevoke == False):
                     with sqlconn.cursor() as cursor:
                        sql = ("DELETE FROM `radcheck` WHERE username = '%s'" % (password))
                        cursor.execute(sql)
                        sqlconn.commit()
                        print("Successfully Exectuted Everyting")
                        os.execv('/home/pi/coinSlot.py', [''])
                        break
                    
        else:
                    with sqlconn.cursor() as cursor:
                        sql = ("SELECT * FROM `radacct` WHERE username = '%s'" % (password))
                        cursor.execute(sql)
                        result = cursor.execute(sql)
                        sqlconn.commit()
                        #print(result)             
finally:
    GPIO.cleanup()
    sqlconn.close()
    while True:
       execfile("/home/pi/coinSlot.py")

