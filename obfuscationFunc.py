#!/usr/bin/python3
# -*- coding: utf-8 -*-

import base64

import random
import string


def obfuscate(strInput):
  enc1=base64.b64encode (bytes(strInput, "utf-8") )
  enc2=''
  for x in range(0,len(enc1)):
    enc2+=chr(enc1[x])+random.choice(string.ascii_letters)
  return enc2

def clear(strInput):
  enc2=''
  for x in range(0,len(strInput)):
    if x % 2 == 0:
      enc2+=(strInput[x])
  #print (enc2)

  enc1=base64.b64decode (bytes(enc2, "utf-8") )
  #print (enc1)
  return enc1


'''
######################################################################################################
'''
def obfuscate2(strInput):
  enc1=base64.b64encode (bytes(strInput, "utf-8") )
  #bytes(base64string, "utf-8")
  #print (enc1)
  idx=0
  enc2=''
  for x in range(0,len(enc1)):
    #randomEntr=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(x))
    #print (randomEntr)
    enc2+=chr(enc1[x])+random.choice(string.ascii_letters)
  #print (enc2)
  return enc2
