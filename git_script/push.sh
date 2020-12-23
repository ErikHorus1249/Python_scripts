#!/bin/bash

GR='\033[0;32m'
NC='\033[0m' # No Color

# ask massage
echo "[+] Message ?"
read mess

if [ -z "$mess" ];
	then
        	echo -e "${GR}[+] Create a new commit containing the current contents with the default message : up ${NC}"
		git add . && git commit -m $mess --branch && git push
	else
        	echo -e "${GR}[+] Create a new commit containing the current contents with the message : $mess ${NC}"
		git add . && git commit -m $mess --branch && git push
    fi

#Reference: https://ryanstutorials.net/bash-scripting-tutorial/bash-loops.php
