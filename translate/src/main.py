# by ErikHorus1249
# pip3 install googletrans==3.1.0a0
# import GG translate API
from googletrans import Translator 
import httpcore
# thuc hien dich
def trans(text_src):
    translator = Translator()
    try :
        result = translator.translate(text_src, src='en', dest='vi')
        return result.text
    except httpcore._exceptions.ConnectError:
        return '+ Checking your network cables, modem, and routers\n+ Reconnecting to your wireless network'
# du lieu dau vao
def getTextSRC():
    return input()

if __name__ == "__main__":
    while(True):
        print('='*37+'\nEn -> Vi :')
        text_src = getTextSRC()
        if text_src.strip()=='e' or text_src.strip()=='exit':
            break
        print('='*37)
        print(trans(text_src))