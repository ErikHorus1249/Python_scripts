#!/bin/bash 

# hightlight green color
make_GR() {
   GR='\033[0;32m'                             
   NC='\033[0m' # No Color
   printf "${GR}[+]$1${NC}\n"                                                                             
}

# hightlight yellow color
make_YL() {
   GR='\033[1;33m'                             
   NC='\033[0m' # No Color
   printf "${GR}[!]$1${NC}\n"                                                                         
}

# #Step 01
# make_GR "Step 1: Update all service..."
# sleep 2
# yum -y update

make_GR "Step 1: Create the volume that Portainer Server will use to store its database:"
docker volume create portainer_data

make_GR "Step 2: Download and install the Portainer Server container:"
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always 
\ -v /var/run/docker.sock:/var/run/docker.sock 
\ -v portainer_data:/data portainer/portainer-ce:latest

make_GR "Step 3: Show docker container:"
docker ps

