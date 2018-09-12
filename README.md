# WifiVendoMachine
Free Architecture for a Wifi Vending Machine

hardware needed:
1. Raspberry pi 3 B / B+
2. Ethernet Cable
3. 16x2 LCD Screen
4. Push button
5. Coin acceptor
6. 12V 1A Power Source
7. Rasberry Pi Power Source


# Hardware setup

**Just follow the hardwareConfig.fzz file**



# Software Setup:

1. fresh install raspbian on your raspberry pi 3 B/B+ and update it.

2. next we will install the hotspot and the captive portal

(https://www.pihomeserver.fr/en/2016/09/15/transformer-raspberry-pi-hotspot-wi-fi-facilement-grace-a-script/)

3. install git
> apt-get install git

> git clone https://github.com/pihomeserver/Pi-Hotspot.git


**RUN THE SCRIPT**

> cd Pi-Hotspot

> chmod +x pihotspot.sh

> ./pihotspot.sh

4. setting up the codes
> Put the python file "CoinSlot.py" and "autostart.sh" into the /home/pi directory. and and chmod +x

5. clone the Adafruit_Python_CharLCD repository
> sudo git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git

6. Install mysql cursors
> sudo apt install python-pip  
> sudo pip install PyMySQL  

7. automate everything. Go to the directory
> cd .config/lxsession/LXDE-pi
> sudo nano autostart

8. add the following code at the end of the file
> /home/pi/autostart.sh



# Customizing your webpages

1. Just locate the following directory
> /usr/share/nginx/html/daloradius for the daloradius interface

> cd /usr/share/nginx/portal/ && sudo leafpad index.html for the webpages



