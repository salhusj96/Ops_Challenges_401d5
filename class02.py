#!/usr/bin/python3

# Script: Ops 401d5 Ops Challenge Solution 
# Author: Jon Salhus                  
# Date of latest revision: 10/5/2022  
# Purpose: creates an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down.
# Source: https://stackoverflow.com/questions/26468640/python-function-to-test-ping

import datetime
import time
import os

def check_ping():
    hostname = "8.8.8.8"
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        pingstatus = "PING OK"
    else:
        pingstatus = "PING ERROR"
    return pingstatus

pingstatus = check_ping()

while True:
    print("Start: %s" % time.ctime())
    check_ping()
    print(pingstatus)
    time.sleep(3)
    print("End: %s" % time.ctime())

