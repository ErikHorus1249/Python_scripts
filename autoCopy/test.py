
import subprocess
import os
import shutil
import time

def getUSB():
    output = subprocess.Popen("lsblk", stdout=subprocess.PIPE, shell=True)
    for out in output.communicate()[0].split():
        if '/media/' in str(out):
            src = str(out).replace("b'","").replace("'","")
            return src
    return "NONE"

def getFileList():
    src = getUSB()
    video_list = []
    if src != "NONE":
        files = os.listdir(src)
        for file in files:
            if "mkv" in file:
                video_list.append(file)
        return video_list
    else:
        return "NO LIST"


status = True
while status:
    dest = "/home/erik/Documents/Python_scripts/autoCopy/store"
    src = getUSB()
    if(src == "NONE"):
        continue
    else:
        videos = getFileList()
        status = False
        for video in videos:
            shutil.copy(src+"/"+video,dest)
            print("Copy successfully %s" % video)
            time.sleep(0.5)





