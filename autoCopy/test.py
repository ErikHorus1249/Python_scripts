
import subprocess
import os
import shutil
import time
import glob

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
            if "png" in file:
                video_list.append(file)
        return video_list
    else:
        return "NO LIST"

def getObject():
    src = getUSB()
    parents = []
    parents.append(src)
    obs = os.listdir(src)
    for ob in obs:
        if '.' != ob:
            getObject
    return ob

def copy(src,dst):
    if shutil.copytree(src, dst, dirs_exist_ok=True):
        return True
    else:
        return False

def getRecursionFile():
    filenames = []
    for filename in glob.glob(str(getUSB()) + '/**/*.mkv'):
        filenames.append(filename)
    return filenames

def getNonRecursionFile():
    filenames = []
    for filename in glob.glob(str(getUSB()) + '/*.mkv'):
        filenames.append(filename)
    return filenames

status = True
while status:
    dest = "/home/erik/Documents/Python_scripts/autoCopy/store"
    src = getUSB()
    if(src == "NONE"):
        continue
    else:
        videos = getRecursionFile() + getNonRecursionFile()
        status = False
        for video in videos:
            shutil.copy(video,dest)
            time.sleep(0.5)




