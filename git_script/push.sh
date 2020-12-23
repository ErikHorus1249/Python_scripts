#!/bin/bash

echo Message ?

read mess

git add . && git commit -m $mess --branch && git push
