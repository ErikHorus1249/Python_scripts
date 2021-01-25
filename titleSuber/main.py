
import re
import time 
import translators as ts 
from multiprocessing import Pool
from googletrans import Translator

f = open("test2.srt","r")
fw = open("result.srt","w")

#f get raw text
raw = f.readline()

store = []
class sub:
    def __init__(self, pos, content):
        self.pos = pos
        self.content = content
    
    def get_content(self):
        return self.content

    def get_pos(self):
        return self.pos


subtitles = []
result_subtitles = []

def translate(title_content):
    translator = Translator()
    return translator.translate(title_content, src='en', dest='vi')


def make_vi_sub(subtitle):
    pattern ='(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})'
    numPattern = '\d+'
    translator = Translator()
    content = subtitle.get_content()
    if content != "\n":
        if re.match(pattern,content) or re.match(numPattern,content) :
            return (subtitle.get_pos(),content)
        else :
            content = re.sub("\\n"," ",content)
            try :
                final_sub = ts.bing(content , from_language='en', to_language='vi')
                return (subtitle.get_pos(),final_sub+"\n"+content+"\n")
            except :
                return (subtitle.get_pos(),content)     
    else:
        return (subtitle.get_pos(),"\n")


        

for num, line in enumerate(f,1):
    sub1 = sub(num,line)
    subtitles.append(sub1)

def myFunc(e):
  return e['pos']

def run():
    num_procs = 64 # the number of threads handled
    pool = Pool(processes=num_procs)
    for res in pool.imap_unordered(make_vi_sub, [nonsub for nonsub in subtitles]):
        if res != None :
            print(res[1])
            result_subtitles.append({"pos":res[0],"content":res[1]})

    result_subtitles.sort(key=myFunc)
    for line in result_subtitles:
        fw.write(line["content"])



if __name__ == '__main__':
    start_time = time.time()
    run()
    print("\n--->  time execution %s s" % round(time.time() - start_time,2))
