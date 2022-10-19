#!/usr/bin/python3

# Script: Ops 401d5 Ops Challenge Solution 13
# Author: Jon Salhus                  
# Date of latest revision: 10/19/2022  
# Purpose: Port Range Scanner and Ping Sweeper

# Imported Libraries
import random
from scapy.all import ICMP, IP, sr, sr1, TCP
from ipaddress import IPv4Network
import sys

host = input("Enter an IP address to scan: ")
port_range = [22, 23, 80, 443, 3389]

def sweeper(host):
        resp = sr1(IP(dst=str(host))/ICMP(),timeout=1,verbose=0)

        if resp is None:
            print(f"{host} is down or not responding. ")
        elif (
            int(resp.getlayer(ICMP).type) == 3 and
            int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
        ):
            print(f"{host} is blocking ICMP traffic.")
        else:
            print(f"{host} is responding.")
            scanner(host, port_range)

def scanner(host, port_range):
    for dst_port in port_range:
        src_port = random.randint(1025,65534)
        resp = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='S'),timeout=1,verbose=0)

        if resp is None:
            print(f"{host}:{dst_port} is filtered (silently dropped).")
        elif (resp.haslayer(TCP)):
            if (resp.getlayer(TCP).flags == 0x12):
                send_rst = sr(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='R'),timeout=1,verbose=0)
                print(f"{host}:{dst_port} is open.")
            elif (resp.getlayer(TCP).flags == 0x14):
                print(f"{host}:{dst_port} is closed.")
        elif (resp.haslayer(ICMP)):
            if (
                int(resp.getlayer(ICMP).type) == 3 and
                int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
            ):
                print(f"{host}:{dst_port} is filtered (silently dropped).")

sweeper(host)
