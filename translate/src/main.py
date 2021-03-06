# by ErikHorus1249
# pip3 install googletrans==3.1.0a0
# import GG translate API
import googletrans
from googletrans import Translator 
import httpcore
import os
import time
import json
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

def get_languages():
    # print(googletrans.LANGUAGES)
    languages = googletrans.LANGUAGES
    for lang in languages:
        print('[+] '+lang+': '+languages[lang])
    src=input("CHOOSE SRC Language :").strip()
    dst=input("CHOOSE DST Language :").strip()
    # kiem tra ho tro ngon ngu
    # support_lang = True
    src_e = ""
    dst_e = ""
    for lang in languages:
        if lang == src:
            src_e = languages[lang]
        if lang == dst:
            dst_e = languages[lang]

    return [src,src_e,dst,dst_e]

def trans(text_src, src, dst):
    # print(googletrans.LANGUAGES)
    translator = Translator()
    # print(languages[1])
    try :
        result = translator.translate(text_src, src=src, dest=dst)
        return result.text
    except httpcore._exceptions.ConnectError:
        return bcolors.WARNING + '+ Checking your network cables, modem, and routers\n+ Reconnecting to your wireless network' + bcolors.ENDC             

# du lieu dau vao
def getTextSRC():
    raw_text = input()
    if raw_text == "":
        return "input is empty"
    else:
        return raw_text

def showLogo():
    cwd = os.getcwd()  # Get the current working directory (cwd)
    #f = open(cwd+"/logo.txt","r")
    f = open("/home/erik/Documents/scripts/translate/src/logo.txt","r")
    logo = "".join(f.readlines())
    print(bcolors.FAIL+logo+bcolors.ENDC)

if __name__ == "__main__":
    # chon ngon ngu
    LANG = get_languages()
    Title = LANG[1] + "----->" + LANG[3]
    # main loop
    while(True):
        # print(bcolors.OKBLUE+'='*37+'\nEn -> Vi :'+bcolors.ENDC)
        try:
            start_time = time.time()
            print(Title)
            text_src = getTextSRC()
            if text_src.strip()=='e' or text_src.strip()=='exit':
                break
            print(bcolors.OKBLUE+'='*50+bcolors.ENDC)
            print(bcolors.OKCYAN+trans(text_src, LANG[0], LANG[2])+bcolors.ENDC)
            print("Time execution : %s s" % round(time.time() - start_time,2)+bcolors.ENDC)
        except KeyboardInterrupt:
            print("press control-c again to quit")
            break 

        
