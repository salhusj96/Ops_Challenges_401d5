#!/usr/bin/python3

# Script: Ops 401d5 Ops Challenge Solution 12
# Author: Jon Salhus                  
# Date of latest revision: 10/18/2022  
# Purpose: Port Range Scanner and Ping Sweeper

# Imported Libraries
import sys 
from scapy.all import IP, sr1, TCP
import random
from ipaddress import IPv4Network

## TCP Port Range Scanner
def scanner():
    host = input("Please enter an IP: ")
    range = [22,23,80,443,1080,3389,5554]
    for dst in range:
        src = random.randint(1025,65534)
    response = sr1(IP(dst=host)/TCP(sport=src,dport=dst,flags="S"),timeout=1,verbose=0)
    print(response)
    if response == None:
        print(str(host)+":"+str(dst)) 
        print("was silently dropped.")
        menu()
    elif(response.haslayer(TCP)):
        if(response.getlayer(TCP).flags == 0x12): 
            print(str(host)+":"+str(dst))
            print("is open.")
            menu()
        if(response.getlayer(TCP).flags == 0x14):
            print(str(host)+":"+str(dst))
            print("is closed.")
            menu()
    else: 
        print(str(host)+":"+str(dst))
        print("was silently dropped")
        menu()


## ICMP Ping Sweeper
def sweeper():
    addr = input("Enter an IP address in CIDR notation: ")
    addr_list = IPv4Network(addr, False)
    print(addr_list)
    for host in addr_list:
        print(host)
        live_count = 0
        op = "s"
    while op == "s":
        op = input("Display all IP addresses in subnet? [y/n]: ")
        if op == "y":
            live_count += 1
            print("Total IP addresses available: "+str(live_count))
            menu()
        else:
            menu()


# Menu Function
def menu():
    options_str = ('Enter 1 to initialize TCP Port Range Scanner\n'
                        'Enter 2 to initialize ICMP Sweep\n'
                        'Enter 3 to exit: ')
    choice = input(options_str)
    return int(choice)

choice = menu()

# Conditionals for Menu
if choice == 1:
    scanner()
elif choice == 2:
    sweeper()
elif choice == 3:
    sys.exit("Exiting program...")
else:
    print("Invalid input, please enter a number on the menu.")
    menu()