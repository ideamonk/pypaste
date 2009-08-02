#!/usr/bin/env python
## pypaste.py -- a command line tool to put codes on pastebins on the fly

# ======================================================================
# Copyright (C) 2009 Abhishek Mishra <ideamonk@gmail.com>
# Time-stamp: Sat Aug  1 20:27:22 IST 2009
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
# ======================================================================

# the above header is based on G0SUB's Python based Gmail checker

import urllib                       # for driving the nuts of the net
import urllib2                      # a new vehicle to ride :)
import sys                          # command line args and other stuff

import pypaste_includes as ppi

version = "1.0"

def pypaste_readconfig():
    ''' reads out the id for pastebin in use '''
    
    try:
        confhandler = open ("pypaste.conf","r")
        ppi.config = confhandler.read()
        confhandler.close()
    except:
        print "Warning: Couldn't access ./pypaste.conf to read configuration from."
        print "Warning: Creating default pypaste.conf ..."
        
        confhandler = open ("pypaste.conf","w")
        confhandler.write ("1")
        confhandler.close()

def pypaste_paste(filename):
    pypaste_readconfig()            # read the id of pastebin in use
    ppi.chunk = ""
    ppi.filename = filename
    
    try:
        filehandle = open (filename,"r")
        ppi.chunk = filehandle.read()
        filehandle.close
                
    except:
        print "Error accessing %s !" % (filename)       
        return
    
    if (len(ppi.chunk) == 0):
        print "Empty files can't be pasted."
        return 
    
    url,values = ppi.prepare_post()
    
    if (url==""):
        print "Failed to fetch your pastebin's url."
        print "Try again after deleting/editing your pypaste.conf"
        return
      
    data = urllib.urlencode(values)
    
    try:                            # there could be connection errors here
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
    except:
        # something went wrong on the otherside
        print "Are you connected yet ?"
        print "If your internet is working fine, then report back to me soon."
        print "Drop a mail on ideamonk at gmail.com"
        print "Specify version %s and pastebin id %s in the mail." % (version,ppi.config)
        return
    
    print response.url
    
    
def parse_args():
    ''' Do what the user wants you do '''    
    if (sys.argv[1] == "--config"):
        pypaste_config()
        
    elif (sys.argv[1] == "--test"):
        pypaste_test()
            
    else:
        # treat it as file to be pasted
        pypaste_paste( sys.argv[1] )    

    
def show_help():
    ''' Shows the usage of pypaste '''
    
    print '''
pypaste 1.0                      author: Abhishek Mishra <ideamonk at gmail.com>

usage: pypaste OPTION [file-to-paste]

OPTIPONS
--------
    --config
        select and configure a pastebin provider from supported list.
        
    --install
        install pypaste.py into your system
    
    --use pastebin_id
        uses a particular available pastebin provider from the list:'''
    
    ppi.showlist()
    

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        # No arguments supplied! -> show help
        show_help()
    else:
        parse_args()
        

