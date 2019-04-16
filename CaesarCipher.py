#!/usr/bin/env python3

### CAESAR CIPHER ###

# The program implements a Caesar cipher, both encoding and decoding. The key is an integer from 1 to 25. 
# This cipher rotates the letters of the alphabet (A to Z). 
# The encoding replaces each letter with the 1st to 25th next letter in the alphabet (wrapping Z to A). 
# For example, key 3 encrypts "ABC" to "DEF".

my_string = "abcdefghijklmnopqrstuvwxyz"

def encrypt(text,key):
    
# This function is used to encrypt the given text.
    
    encrypt_string = "abcdefghijklmnopqrstuvwxyz" * 2
    output = ""
    
    for char in text:
        
        if char in my_string:
            
            index = encrypt_string.index(char)
            output += encrypt_string[index + key]
            
        else:
            
            output += char
        
    return output

def decrypt(text,key):
    
# This function is used to decrypt the given text.
    
    decrypt_string = "zyxwvutsrqponmlkjihgfedcba" * 2
    output = ""
    
    for char in text:
        
        if char in my_string:
            
            index = decrypt_string.index(char)
            output += decrypt_string[index + key]
            
        else:
            
            output += char
            
    return output

# At the final step, we define the user's choices and make the program ready for use.

if __name__ == '__main__':
    
    print(" Enter 1 to encrypt a text\n Enter 2 to decrypt a text\n Enter 3 to do them both\n ")
    
    choice = int(input("Please enter a choice: "))
    
    if choice == 1:
        
        string_txt = input("Enter the text you want to encrypt: ")
        key = int(input("Enter a key between 1-25: "))
        
        print("The encrypted text is: ")
        print(encrypt(string_txt, key))
        
    elif choice == 2:
        
        string_txt = input("Enter the text you want to decrypt: ")
        key = int(input("Enter a key between 1-25: "))
        
        print("The decrypted text is: ")
        print(decrypt(string_txt, key))
        
    elif choice == 3:
        
        string_txt = input("Enter the text you want to encrypt and decrypt at the same time: ")
        key = int(input("Enter a key between 1-25: "))
        
        print("The encrypted text is: ")
        print(encrypt(string_txt, key))
        
        print("The decrypted text is: ")
        print(decrypt(string_txt, key))
        
    else:
        
        print("Your choice is invalid. Please try again!")
