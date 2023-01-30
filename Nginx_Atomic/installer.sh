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

#Step 01
make_GR "Step 1: Update all service..."
sleep 2
yum -y update

#Step 2
make_GR "Step 2: Create the /etc/ssl/nginx directory..."
sleep 2
# scp /root/nginx-repo.* root@ng2:/root
mkdir -p /etc/ssl/nginx
cd /etc/ssl/nginx

#Step 3
make_YL "Step 3: Log in to MyF5 Customer Portal and download your nginx-repo.crt and nginx-repo.key files"
sleep 2
cp /root/nginx-repo.* /etc/ssl/nginx/

# Step 4
make_GR "Step 4: Install the required ca-certificates dependency..."
sleep 2
make_GR "Execute: yum install -y ca-certificates install epel-release wget"
yum install -y ca-certificates install epel-release wget 

# Step 5
make_GR "Step 5: Copy the nginx-repo.crt and nginx-repo.key files to the /etc/ssl/nginx/ directory..."
sleep 2

# Step 6
make_GR "Step 6: Add NGINX Plus repository by downloading the nginx-plus-amazon2.repo file to /etc/yum.repos.d ..."
sleep 2
wget -P /etc/yum.repos.d https://cs.nginx.com/static/files/nginx-plus-7.4.repo

# Step 7
make_GR "Step 7: Install the nginx-plus package. Any older NGINX Plus package is automatically replaced..."
sleep 2
yum install nginx-plus nginx-ha-keepalived -y

# Step 8
make_GR "Step 8: Install the ModSecurity module..."
sleep 2
yum install nginx-plus-module-modsecurity -y

make_YL "Step 9: Check the nginx binary version to ensure that you have NGINX Plus installed correctly..."
sleep 2
systemctl enable nginx.service
systemctl start nginx.service
nginx -v

make_GR "Step 10: Remove old rules and copy contents to the rule config directory..."
MOD_DIR=/etc/httpd/modsecurity.d/
if [ -d "$MOD_DIR" ];
then
    make_YL "$MOD_DIR directory exists."
    make_GR "Deleting $MOD_DIR directory..."
else
  make_GR "$DIR directory does not exist."
   make_GR "Creating $MOD_DIR directory..."
   mkdir -p $MOD_DIR
fi

make_GR "Step 11: Download/Extract ruleset from: https://updates.atomicorp.com/channels/rules/nginx-latest/"
read -p "Your name? " USERNAME
read -sp "Enter your password to continue!" PASSWORD
make_GR "$USERNAME"
make_GR "$PASSWORD"
# curl -o nginx-waf-202301102304.tar.gz https://updates.atomicorp.com/channels/rules/nginx-latest/nginx-waf-202301102304.tar.gz -u kietnguyen:rNeR7i3cajW4je

make_GR "--------------------Done------------------------"