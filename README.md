# NIKON-USB-shuttercontrol

**Why this project**

The Nikon D90 can be controlled from Kstart/Ekos for taking astrophotograpy but is limited to 30 seconds shuttertime.
As astrophotography typically requires a longer shuttertime, the use of an external shuttercable is required.
However, because I prefer to work remotely, it's important for me to be able to preview the photo's.  To allow this, a cable is required that will work in sync withe Kstars so when shutter closes, Kstars can download the data.

**Used for this project:**
- USBRELAY (For example https://www.amazon.com/Relays-Channel-Programmable-Computer-Control/dp/B08CZRT6N8)
- Nikon Shutter release cable (to cut and use)  (For example: https://www.amazon.com/Zeikos-ZE-MCDC2-Control-Shutter-Release/dp/B002UD4OB6)

The physical cabling is easy, the yellow and red cable are combined together in a "NO" (normally open) contact while white is the other contact.
So when the USBRELAY device is activated, the relay is activated and the shutter is open.
(see also https://www.cloudynights.com/topic/457536-usb-corded-shutter-control-for-nikon/ but the USB to serial didn't work for me)

**How is code build**

As I am not used to work with C and I prefer not to create script in Bash, I have preferred to work with Python.  However, Kstars/Ekos don't have native Python support.  I didn't wanted to recompile the code and I wanted to stay as close to the original code so the only option was to use the API's of Indi.

When you want to interact with Kstars/Ekos, you can use three commands as part of the Indi driver stack:
https://indilib.org/develop/developer-manual/104-scripting.html

The main challenge is that these commands are console based so it requires some tricks to integrate this in the Python code.
The first command in the code is a wait loop until Kstars/Ekos is triggered while the second command is used to retreive all the settings of Kstars/Ekos including the shutter timer and to use this in the actions for USBrelay.

*Additional compilation*
For Ubunutu (on pc or Raspberry):  apt-get install usbrelay
(note that the usbrelay command as part of apt is buggy, compilation from code may be required)


