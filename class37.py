#!/usr/bin/python3

# Script: Ops 401d5 Ops Challenge Solution 37
# Author: Jon Salhus                  
# Date of latest revision: 11/22/2022
# Purpose: Web Application Fingerprinting Part 2 of 3

# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import requests
import webbrowser

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Add here some code to make this script perform the following:
# - Send the cookie back to the site and receive a HTTP response
s = requests.Session()
r = requests.get(targetsite, cookies=cookie)
# - Generate a .html file to capture the contents of the HTTP response
f = open('cookietest.html', 'w')
f.write(r.text)
f.close
# - Open it with Firefox
webbrowser.open('cookietest.html')