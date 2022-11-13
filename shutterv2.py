import time
import os

#create the SNAP support
Shutter_open = "indi_setprop \"EQMod Mount.SNAPPORT1.SNAPPORT1_ON=On\""
Shutter_close = "indi_setprop \"EQMod Mount.SNAPPORT1.SNAPPORT1_OFF=On\""

#Create a dummy tty port to exchange information
software,pseudo = os.openpty()
print("software: ", software, " pseudo",pseudo)
fd_pseudo = os.ttyname(pseudo)
print("Make sure that your user have access to tty with command \"adduser [username] tty\" ")
print("port for shutter release in Ekos: ", fd_pseudo)

#Put the USBrelay on off before starting the program
os.system("usbrelay nikon_1=0")

while True:
    read = list(os.read(software,3))
    if read[2]:
        print("Shutter open")
        os.system("usbrelay nikon_1=1")
        os.system(Shutter_open)
    else:
        print("Shutter closed")
        os.system("usbrelay nikon_1=0")
        os.system(Shutter_close)
    time.sleep(0.01)