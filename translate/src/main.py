# by ErikHorus1249
# pip3 install googletrans==3.1.0a0
# import GG translate API

from googletrans import Translator 
import httpcore
import os
import time
# thuc hien dich

# mau cho text
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def trans(text_src):
    translator = Translator()
    try :
        result = translator.translate(text_src, src='en', dest='vi')
        return result.text
    except httpcore._exceptions.ConnectError:
        return bcolors.WARNING + '+ Checking your network cables, modem, and routers\n+ Reconnecting to your wireless network' + bcolors.ENDC             
# du lieu dau vao
def getTextSRC():
    return input()

def showLogo():
    cwd = os.getcwd()  # Get the current working directory (cwd)
    #f = open(cwd+"/logo.txt","r")
    f = open("/home/erik/Documents/scripts/translate/src/logo.txt","r")
    logo = "".join(f.readlines())
    print(bcolors.FAIL+logo+bcolors.ENDC)

if __name__ == "__main__":
    # showLogo()
    while(True):
        print(bcolors.OKBLUE+'='*37+'\nEn -> Vi :'+bcolors.ENDC)
        start_time = time.time()
        text_src = getTextSRC()
        if text_src.strip()=='e' or text_src.strip()=='exit':
            break
        print(bcolors.OKBLUE+'='*37+bcolors.ENDC)
        print(bcolors.OKCYAN+trans(text_src)+bcolors.ENDC)
        print("Time execution : %s s" % round(time.time() - start_time,2)+bcolors.ENDC)
