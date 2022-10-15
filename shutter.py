from asyncio import subprocess
import os
import time
import subprocess


print("programma is gestart")
while True:
    os.system("indi_eval -t 0 -w \'\"GPhoto CCD.CCD_EXPOSURE.CCD_EXPOSURE_VALUE\"\'>0.001")

#subprocess.run(["indi_eval", " -t 0 -o \'\"GPhoto CCD.CCD_EXPOSURE.CCD_EXPOSURE_VALUE\"\'"])
#print("trigger received", Value)

    result = subprocess.run('indi_getprop',stdout=subprocess.PIPE)
    resultString = list(result.stdout.decode("utf-8").split("\n"))

    for matching in resultString:   
        if "CCD_EXPOSURE_VALUE=" in matching:
            value = matching.find("=")
            ExposureTimer = int(float(matching[43:]))
            print(ExposureTimer)

    os.system("usbrelay nikon_1=1")
    time.sleep(ExposureTimer)
    os.system("usbrelay nikon_1=0")
    time.sleep(5)


