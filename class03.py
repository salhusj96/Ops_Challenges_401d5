#!/usr/bin/python3

# Script: Ops 401d5 Ops Challenge Solution 
# Author: Jon Salhus                  
# Date of latest revision: 10/5/2022  
# Purpose: A script that automatically sends an e-mail notification based on the ping status of a host, input by the user

import smtplib
import datetime
import time
import os

user_email = input("What is your email? ")
user_pw = input("What is the password for the email? ")
hostname = input("Enter an IP address to be pinged. ")
current_ping = 0
last_ping = 0

def check_ping():
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        print(datetime.datetime.now(), hostname, 'HOST UP')
    else:
        print(datetime.datetime.now(), hostname, 'HOST DOWN')
    time.sleep(5)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()

server.login(user_email, user_pw)

def status_up():
    datetime.datetime.now()
    msg = "HOST IS UP!"
    server.sendmail('bsops22@gmail', user_email, msg)
    server.quit()

def status_down():
    datetime.datetime.now()
    msg = "HOST IS DOWN!"
    server.sendmail('bsops22@gmail', user_email, msg)
    server.quit()

while True:
    current_ping == check_ping()
    if current_ping == last_ping:
        if current_ping == True:
            status_down()
        if current_ping == False:
            status_up()
    last_ping = current_ping