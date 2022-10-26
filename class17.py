#!/usr/bin/python3

# Script: Ops 401d5 Ops Challenge Solution 17
# Author: Jon Salhus                  
# Date of latest revision: 10/25/2022  
# Purpose: a custom tool that performs brute force attacks part 2

# Imported Libraries
from pexpect import pxssh
import time
import getpass
import sys
import os


# Menu Function
def menu():
    print('Enter 1 to initialize the Dictionary Iterator\n'
        'Enter 2 to initialize Password Recognition\n'
        'Enter 7 to exit')
    choice = input("Choose: ")
    if choice == "1":
        iterate()
    elif choice == "2":
        checker()
    elif choice == "3":
        print("Secret function initialized. Activating hack.")
        hacker()
    else:
        sys.exit

# Functions
def iterate():
    path = input("Enter your dictionary's filepath:\n")
    file = open(path)
    line = file.readline()
    print(line)
    # Loop
    while line:
        line = line.rstrip()
        word = line
        print(word)
        time.sleep(1)
        line = file.readline()
    file.close
    menu()

def checker():
    pw = getpass.getpass("Enter a password: ", stream = None)
    plist = input("Enter your dictionary's filepath:\n")
    with open(plist) as plist:
        data = plist.read()
        if pw in data:
            print("Password {pw} located in dictionary.")
            menu()
        else:
            print("Password {pw} could not be located.")
            menu()

def hacker():
    session = pxssh.pxssh()
    host = input("Enter an IP address: ")
    user = input("Enter a username: ")
    pwd = getpass.getpass(prompt = "Enter a password: ")

    try:
        session.login(host, user, pwd)
        session.sendline('uptime')
        session.prompt()
        print(session.before)
        session.sendline('whoami')
        session.prompt()
        print(session.before)
        session.sendline('ls-l')
        session.prompt()
        print(session.before)
        session.logout()
    except pxssh.ExceptionPxssh as e:
        print("pxssh failed on login.")
        print(e)

# Calls menu function
menu()