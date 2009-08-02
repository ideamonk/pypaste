## pypaste_includes.py -- helper for pypaste.py
# Sun Aug  2 02:12:12 IST 2009            Abhishek Misha <ideamonk at gmail.com>

# This module provides extensibility over more pastebin services
# To add more services to pypaste.py, all one would need is to append
# a module in this file and write code for that particular service.

import sys
import os
import pwd
import string

sys.path.append ("./modules")   # to allow further imports
import paste_ubuntu_com
import paste_pocoo_org
import dpaste_com

chunk = ""
filename = ""
user = pwd.getpwuid(os.getuid()).pw_name

# configured pastebin service id -
config = '1'                        # by default first pastebin is used            

# uncomment the following if you've a nickname of your choice
#user = 'Your nickname'

def prepare_post():
    global config
    config = config.rstrip()
    
    if config=='1':
        # paste.ubuntu.com
        return paste_ubuntu_com.prepare(filename.split(".")[-1].lower(),user,chunk)
    if config=='2':
        # paste.pocoo.com
        return paste_pocoo_com.prepare(filename.split(".")[-1].lower(),user,chunk)
    if config=='3':
        # dpaste.com
        return dpaste_com.prepare (filename,filename.split(".")[-1].lower(),user,chunk)
    return "",
