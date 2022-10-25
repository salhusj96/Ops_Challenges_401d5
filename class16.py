#!/usr/bin/python3

# Script: Ops 401d5 Ops Challenge Solution 16
# Author: Jon Salhus                  
# Date of latest revision: 10/24/2022  
# Purpose: a custom tool that performs brute force attacks part 1

# Imported Libraries
import time
import getpass
import sys

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
            print("Paassword {pw} could not be located.")
            menu()

# Calls menu function
menu()