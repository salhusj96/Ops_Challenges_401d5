#!/usr/bin/python3

# Script: Ops 401d5 Ops Challenge Solution 44
# Author: Jon Salhus                  
# Date of latest revision: 12/5/2022
# Purpose: Simple Port Scanner

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 1
sockmod.settimeout(timeout)

hostip = input("Please enter an IP address:\n")
pinput = input("Please enter a port number:\n")
portno = int(pinput)

def portScanner(portno):
    if sockmod.connect_ex((hostip, portno)):
        print("Port closed")
    else:
        print("Port open")

portScanner(portno)
