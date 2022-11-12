import time
import os
software,pseudo = os.openpty()
print("software: ", software, " pseudo",pseudo)
fd_pseudo = os.ttyname(pseudo)
print("Make sure that your user have access to tty with command \"adduser [username] tty\" ")
print("port for shutter release in Ekos: ", fd_pseudo)
os.system("usbrelay nikon_1=0")

while True:
    read = list(os.read(software,3))
    if read[2]:
        print("Shutter open")
        os.system("usbrelay nikon_1=1")
    else:
        print("Shutter closed")
        os.system("usbrelay nikon_1=0")
    time.sleep(0.01)