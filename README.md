# NIKON-USB-shuttercontrol

**Why this project**

The Nikon D90 can be controlled from Kstart/Ekos for taking astrophotograpy but is limited to 30 seconds shuttertime.
As astrophotography typically requires a longer shuttertime, the use of an external shuttercable is required.
However, because I prefer to work remotely, it's important for me to be able to preview the photo's.  To allow this, a cable is required that will work in sync withe Kstars so when shutter closes, Kstars can download the data.

**Used for this project:**
- USBRELAY (For example https://www.amazon.com/Relays-Channel-Programmable-Computer-Control/dp/B08CZRT6N8)
- Nikon Shutter release cable (to cut and use)  (For example: https://www.amazon.com/Zeikos-ZE-MCDC2-Control-Shutter-Release/dp/B002UD4OB6)

**How is code build**

As I am not used to work with C and I prefer not to create script in Bash, I have preferred to work with Python.  However, Kstars/Ekos don't have native Python support.  I didn't wanted to recompile the code and I wanted to stay as close to the original code so the only option was to use the API's of Indi.

When you want to interact with Kstars/Ekos, you can use three commands as part of the Indi driver stack:
https://indilib.org/develop/developer-manual/104-scripting.html

The main challenge is that these commands are console based so it requires some tricks to integrate this in the Python code.

*Additional compilation*



