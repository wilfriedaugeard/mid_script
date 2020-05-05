#!/usr/bin/env python3
import subprocess
import os


# Git
sslstrip_clone = 'git clone https://github.com/moxie0/sslstrip'
dns2proxy_clone = 'git clone https://github.com/LeonardoNve/dns2proxy'

# Check directory
ls = os.listdir()

get_sslstrip = False
get_dns2proxy = False

for d in ls:
    if(d == 'sslstrip'):
        get_sslstrip = True
    if(d == 'dns2proxy'):
        get_dns2proxy = True

if(not get_sslstrip):
    try:
        subprocess.check_output(sslstrip_clone.split(' '))
    except: 
        print("Oops ! An error occured.. You can use the following command: "+sslstrip_clone)
if(not get_dns2proxy):
    try:
        subprocess.check_output(dns2proxy_clone.split(' '))
    except: 
        print("Oops ! An error occured.. You can use the following command: "+dns2proxy_clone)