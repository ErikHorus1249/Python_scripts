#!/bin/bash

GR='\033[0;32m'
NC='\033[0m' # No Color

now=$(date +"%T")

# ask massage
echo "[+] Message ?"
read mess

if [ -z "$mess" ];
	then
		git add .
		echo -e "${GR}[+] $now: Successfully added content${NC}"
		git commit -m $mess -q
        	echo -e "${GR}[+] $now: Create a new commit containing the current contents with the default message : up ${NC}"
		git push -q
		echo -e "${GR}[+] $now: Successfully pushed${NC}"
	else
		git add .
                echo -e "${GR}[+] $now: Successfully added content${NC}"
                git commit -m $mess -q
                echo -e "${GR}[+] $now: Create a new commit containing the current contents with the default message : up ${NC}"
                git push -q
                echo -e "${GR}[+] $now: Successfully pushed${NC}"
    fi

echo -e "${GR}[+] $now: DONE!${NC}"
#Reference: https://ryanstutorials.net/bash-scripting-tutorial/bash-loops.php
