
import re
import time 
from multiprocessing import Pool
from googletrans import Translator
import pydeepl

f = open("The.Kings_.Man_.2021.1080p.WEB-DL.DDP5_.1.Atmos_.H.264-EVO.srt","r", encoding='utf-8')
# with open(file=, encoding='utf8') as f:
fw = open("result.srt","w", encoding='utf-8')

#f get raw text
raw = f.readline()

TIME_PATTERN ='(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})'
NUMBER_PATTERN = '\d+'
# list for storing data
SUBTITLES = []
FINAL_SUBTITLE = []

# class for nonsub data
class Subtitle:
    def __init__(self, pos, content):
        self.pos = pos
        self.content = content
    
    def get_content(self):
        return self.content

    def get_pos(self):
        return self.pos



# translate function
def translate(title_content):
    translator = Translator()
    return (translator.translate(title_content, src='en', dest='vi')).text

# get data from file 
SUBTITLES = [Subtitle(num, line)  for num, line in enumerate(f,1)]

def translating(subtitle: Subtitle) -> None:
    content = subtitle.content
    if not re.match(TIME_PATTERN,content) and not re.match(NUMBER_PATTERN,content) and content != '\n':
        data = {"pos":subtitle.pos,"content":f'{translate(subtitle.content)} \n'} if content != "Your Grace." else {"pos":subtitle.pos,"content":f'Thưa ngài. \n'}
        print(data)
        return data
    elif content == '\n':
        return {"pos":subtitle.pos,"content":"\n"}
    else:
        return {"pos":subtitle.pos,"content":content}
        
if __name__ == '__main__':
    start_time = time.time()
    num_proc = 20
    FINAL_SUBTITLE = [data for data in Pool(processes=num_proc).imap_unordered(translating, [nonsub for nonsub in SUBTITLES])]    
    FINAL_SUBTITLE.sort(key=lambda x: x['pos'])
    for subtitle in FINAL_SUBTITLE:
        fw.write(subtitle["content"])
    
    print("\n--->  time execution %s s" % round(time.time() - start_time,2))