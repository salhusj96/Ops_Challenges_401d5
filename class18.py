#!/usr/bin/python3

# Script: Ops 401d5 Ops Challenge Solution 18
# Author: Jon Salhus                  
# Date of latest revision: 10/26/2022  
# Purpose: a custom tool that performs brute force attacks part 2

# Imported Libraries
from pexpect import pxssh
import time
import getpass
import sys
from tqdm import tqdm
import zipfile


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
        print("[!] Secret function initialized. Activating SSH brute.")
        hacker()
    elif choice == "4":
        print("[!] Secret function initialized. Activating zip cracker.")
        zipcrack()
    else:
        sys.exit

# Functions
def iterate():
    path = input("[?] Enter your dictionary's filepath:\n")
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
    pw = getpass.getpass("[?] Enter a password:\n")
    plist = input("[?] Enter your dictionary's filepath:\n")
    with open(plist) as f:
        data = f.readlines()
    for line in data:
        if pw in line:
            print("[+] Password " + str(pw) + " located in dictionary.")
            menu()
        else:
            print("[!] Password " + str(pw) + " could not be located.")
            menu()

def hacker():
    session = pxssh.pxssh()
    host = input("[?] Enter an IP address: ")
    user = input("[?] Enter a username: ")
    pwd = getpass.getpass(prompt = "[?] Enter a password: ")

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
        print("[x] pxssh failed on login.")
        print(e)

def zipcrack():
    plist = input("[?] Enter your dictionary's absolute filepath:\n")
    zip_file = input("[?] Enter your zipfile's absolute filepath:\n")
    zip_file = zipfile.ZipFile(zip_file)
    numlist = len(list(open(plist, "rb")))
    print("[!] Total passwords to be tested:", numlist)
    with open(plist, "rb") as plist:
        for word in tqdm(plist, total = numlist, unit = "word"):
            try:
                zip_file.extractall(pwd = word.strip())
            except:
                    continue
            else:
                print("[+] Password found:", word.decode().strip())
                exit(0)
        print("[x] Password not found, try another dictionary.")

                    

# Calls menu function
menu()