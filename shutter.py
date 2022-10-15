from asyncio import subprocess
import os
import time
import subprocess


print("program has started")

# The first line is required to detect when a new recording is started in Kstars/Ekos.  As os.system doesn't support feedback, it's only a trigger.
while True:
    os.system("indi_eval -t 0 -w \'\"GPhoto CCD.CCD_EXPOSURE.CCD_EXPOSURE_VALUE\"\'>0.001")


# When a recording is started, we download all settings of Kstars/Indi, we load this into a list and filter out the actual exposure time
    result = subprocess.run('indi_getprop',stdout=subprocess.PIPE)
    resultString = list(result.stdout.decode("utf-8").split("\n"))

    for matching in resultString:   
        if "CCD_EXPOSURE_VALUE=" in matching:
            value = matching.find("=")
            ExposureTimer = int(float(matching[43:]))
            print(ExposureTimer)

# we activate the relay so the camera is trigger (combine the focus/trigger cable)
    os.system("usbrelay nikon_1=1")
    time.sleep(ExposureTimer)
    os.system("usbrelay nikon_1=0")
    time.sleep(5)


