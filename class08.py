#!/usr/bin/env python3

# Script: Ops 401d5 Ops Challenge Solution 08
# Author: Jon Salhus                  
# Date of latest revision: 10/12/2022  
# Purpose: Intended to be added to my previous script, but simulates a popup window and background change like ransomware

# imports the necessary libraries to interact with windows
import ctypes
import urllib.request

# function that creaters the popupwindow
def popup_window():
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Uh oh! Looks like you got hacked!', 'HACKED!', 0)

# function that was supposed to change the background
def change_desktop_background(user):
        imageUrl = 'https://images.idgesg.net/images/article/2018/02/ransomware_hacking_thinkstock_903183876-100749983-large.jpg'
        # Go to specif url and download+save image using absolute path
        path = f'{user.sysRoot}Desktop/background.jpg'
        urllib.request.urlretrieve(imageUrl, path)
        SPI_SETDESKWALLPAPER = 20
        # Access windows dlls for funcionality eg, changing dekstop wallpaper
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)
        
popup_window()
change_desktop_background(user)