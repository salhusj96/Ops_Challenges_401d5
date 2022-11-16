#!/usr/bin/python3

# Script: Ops 401d5 Ops Challenge Solution 31
# Author: Jon Salhus                  
# Date of latest revision: 11/15/2022
# Purpose: Detect file names and locatons on both Windows and Linux systems

from sys import platform
import os, time


# Functions
# Linux
def linSearch():
    prompt_file = input("Provide a target file path:\n")
    prompt_dir = input("Provide a target directory path:\n")
    for root, dir, files in os.walk(prompt_dir):
        if prompt_file in files:


# Windows
def winSearch():

# Determine OS and run appropriate function
if platform == "linux" or "platform" == "linux2":
    print("You are operating within Linux")
    linSearch()
elif platform == "win32":
    print("You are operating within Windows")
    winSearch()