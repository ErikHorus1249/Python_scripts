#!/bin/bash

RED='\033[0;31m'
NC='\033[0m' # No Color

# ask massage
echo Message ?

read mess

echo -e "${RED}Create a new commit containing the current contents with the message : $mess ${NC}" 
git add . && git commit -m $mess --branch && git push
