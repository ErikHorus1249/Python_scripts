#!/bin/bash

echo Message ?

read mess

echo Create a new commit containing the current contents with message : $mess 
git add . && git commit -m $mess --branch && git push
