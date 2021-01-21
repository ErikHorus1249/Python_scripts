import googletrans
from googletrans import Translator 
import re
import time 
import translators as ts 

f = open("test.srt","r")
fw = open("result.srt","w")

#f get raw text
raw = f.readline()

def trans(text_src):
#    print(googletrans.LANGUAGES)
    translator = Translator()
    # print(languages[1])
    try :
        result = translator.translate(text_src, src='en', dest='vi')
        return result.text
    except :
        return text_src 

print(trans("Starting . . ."))

store = []
pattern ='(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})'
numPattern = '\d+'
for line in f:
    if line!='\n':
        if re.match(pattern,line) or re.match(numPattern, line):
            store.append(line)
            #print(raw_line)
        else:
            raw_line = re.sub('\\n',' ',line)
            result  = ts.google(raw_line,from_language='auto',to_language='vi')
            print(result)
            store.append(result+"\n")
           # fw.write(result+"\n")
    else:
        store.append("\n")
        #fw.write("\n")
for line in store:
    fw.write(line)
print("Translating . . .")
