#!/usr/bin/python3

# Script: Ops 401d5 Ops Challenge Solution 11 
# Author: Jon Salhus                  
# Date of latest revision: 10/17/2022  
# Purpose: a TCP Port range scanner that tests whether a range of TCP ports are open or closed

# Imports necessary libraries
from sys import flags
from scapy.all import IP, sr1, TCP
import random

# Declaration of variables
host=input("Please enter an IP: ")
range=[22,23,80,443,1080,3389,5554]

# For Loop
for dst in range:
    src=random.randint(1025,65534)
    response=sr1(IP(dst=host)/TCP(sport=src,dport=dst,flags="S"),timeout=1,verbose=0,)
    print(response)

# Conditionals
    if response==None: 
        print(str(host)+":"+str(dst)) 
        print("DROPPED")
    elif(response.haslayer(TCP)): 
        if(response.getlayer(TCP).flags == 0x12): 
            print(str(host)+":"+str(dst))
            print("OPEN")
        if(response.getlayer(TCP).flags == 0x14):
            print(str(host)+":"+str(dst))
            print("CLOSED")
    else: 
        print(host+":"+dst)
        print("DROPPED")