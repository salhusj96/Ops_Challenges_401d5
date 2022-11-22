#!/usr/bin/python3

# Script: Ops 401d5 Ops Challenge Solution 36
# Author: Jon Salhus                  
# Date of latest revision: 11/22/2022
# Purpose: Web Application Fingerprinting Part 1 of 3

import socket
import time
import subprocess

# net cat function
def netcat(a, p):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((a, int(p)))

    run = "nc" + a + " " + p
    sock.sendall(run.encode())


    # While Loop
    while True:
        data = sock.recv(1024)
        if (not data):
            break
        res += data.decode()

    print(res)

    sock.close()