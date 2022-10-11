#!/usr/bin/python3

# Script: Ops 401d5 Ops Challenge Solution 
# Author: Jon Salhus                  
# Date of latest revision: 10/10/2022  
# Purpose: A script that prompts the user to select a mode of encryption/decryption, and performs a function based on the input

# imports fernet, cryptography and path libraries
from cryptography.fernet import Fernet
import os.path
from os.path import exists

# checks if the key exists. if it does not, generates the key. if it does, it loads the key
file_exists = os.path.exists('key.key')
print('Key Status: ')
print(file_exists)
if file_exists == False:
    def write_key():
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    write_key()
else:
    def load_key():
        return open("key.key", "rb").read() 
# Loads the key and initializes Fernet
key = load_key()
f = Fernet(key)

# menu function
def menu():
    options_str = ('Enter 1 to Encrypt a file\n'
                        'Enter 2 to Decrypt a file\n'
                        'Enter 3 to Encrypt a message\n'
                        'Enter 4 to Decrypt a message\n'
                        'Enter 5 to exit: ')
    choice = input(options_str)
    return int(choice)


# encryption/decryption conditionals
choice = menu()
if choice == 1:
    def enc_file():
        filepath = input("Please enter the filepath of the file you wish to encrypt: ")
        with open(filepath, 'rb') as file:
                original = file.read()
        encrypted = f.encrypt(original)
        with open(filepath, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
    enc_file()
elif choice == 2:
    def dec_file():
        filepath = input("Please enter the filepath of the file you wish to decrypt: ")
        with open(filepath, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
        decrypted = f.decrypt(encrypted)
        with open(filepath, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
    dec_file()
elif choice == 3:
    def enc_str():
        message = input("Please enter some plain text: ").encode()
        print("Plaintext is: " + str(message.decode('utf-8')))
        encrypted = f.encrypt(message)
        print("Ciphertext is: " + str(encrypted.decode('utf-8')))
    enc_str()
elif choice == 4:
    def dec_str():
        message = input("Please enter ciphertext: ").encode()
        print("Ciphertext is: " + str(message.decode('utf-8')))
        decrypted = f.decrypt(message)
        print("Plaintext is: " + str(decrypted.decode('utf-8')))
    dec_str()
elif choice == 5:
    print("Exiting script.")