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
    # ask user for path

    # ask user for filename

    # count num of files searched, stored in var

    # count num of files found, stored in var

    # print vars


# Windows
def winSearch():
    # ask user for path

    # ask user for filename

# Determine OS and run appropriate function
if platform == "linux" or "platform" == "linux2":
    print("You are operating within Linux")
    linSearch()
elif platform == "win32":
    print("You are operating within Windows")
    winSearch()