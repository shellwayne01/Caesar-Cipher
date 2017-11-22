#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 00:03:19 2017

@author: yorranshellwattson
"""
#Caesar cipher using dictionaries with my last name as keys
#to get encrypted and decrypted stactements. 

#Set of characters that will serve as the "alphabet" for this caesar cipher.
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
'q','r','s','t','u','v','w','x','y','z',' ','.',',','?','!']

def getIndex(letter):
    x = alphabet.index(letter)
    return x
 
#Encrypts a statement    
def encrypt(original):
    word = ""
    encrypted = ""
    for i in original:
        word += i.lower() #Converts all characters to lowercase
    for i in word:
        encrypted += alphabet[(getIndex(i) + 5) % 31] #Encrypts the lowercase statement
    return encrypted
        
#Decrypts a statement
def decrypt(word):
    decrypted = ""
    for i in word:
        decrypted += alphabet[(getIndex(i) - 5) % 31] #Decrypts to original lowercase statement
    return decrypted

dict1 = {"Wattson": encrypt("Lets encrypt this message!")}
dict2 = {"Wattson": decrypt(dict1["Wattson"])}
        
print(dict1["Wattson"]) #Prints encrypted message
print(dict2["Wattson"]) #Prints decrypted message
