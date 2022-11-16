#!/usr/bin/python3

# Script: Ops 401d5 Ops Challenge Solution 32
# Author: Jon Salhus                  
# Date of latest revision: 11/15/2022
# Purpose:

import hashlib

filename = input("Provide a file path:\n")
def hash_file(filename):
    h = hashlib.sha256()
    with open(filename, 'rb') as file:
        block = 0
        while block != b'':
            block = file.read(1024)
            h.update(block)
            print(h)
        return h.hexdigest()

message = hash_file(filename)
print(message)
