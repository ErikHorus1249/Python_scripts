# by ErikHorus1249
# pip3 install googletrans==3.1.0a0
# import GG translate API
from googletrans import Translator 

# thuc hien dich
def trans(text_src):
    translator = Translator()
    result = translator.translate(text_src, src='en', dest='vi')
    print('='*37)
    print(result.text)

# du lieu dau vao
def getTextSRC():
    return input()

if __name__ == "__main__":
    print("\nEn -> Vi :")
    print('='*37)
    trans(input())