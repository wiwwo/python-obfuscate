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

  enc1=base64.b64decode (bytes(enc2, "utf-8") )
  return enc1


'''
######################################################################################################
'''
def obfuscate2(strInput):
  enc1=base64.b64encode (bytes(strInput, "utf-8") )
  enc2=''
  for x in range(0,len(enc1)):
    randomEntr=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(x))
    enc2+=chr(enc1[x])+randomEntr
  return enc2

def clear2(strInput):
  enc2=''
  idx=0
  stopAt=len(strInput)
  for x in range(1,stopAt):
    if (idx >=  stopAt): break
    enc2+=(strInput[idx])
    for y in range(0,x): idx+=1

  enc1=base64.b64decode (bytes(enc2, "utf-8") )
  return enc1


'''
######################################################################################################
This is obfuscate2, renamed obfuscate3 and ITS DECLARATION is base64-ed
Same with clear3
'''

exec (base64.b64decode ('ZGVmIG9iZnVzY2F0ZTMoc3RySW5wdXQpOgogIGVuYzE9YmFzZTY0LmI2NGVuY29kZSAoYnl0ZXMoc3RySW5wdXQsICJ1dGYtOCIpICkKICBlbmMyPScnCiAgZm9yIHggaW4gcmFuZ2UoMCxsZW4oZW5jMSkpOgogICAgcmFuZG9tRW50cj0nJy5qb2luKHJhbmRvbS5jaG9pY2Uoc3RyaW5nLmFzY2lpX2xldHRlcnMgKyBzdHJpbmcuZGlnaXRzKSBmb3IgXyBpbiByYW5nZSh4KSkKICAgIGVuYzIrPWNocihlbmMxW3hdKStyYW5kb21FbnRyCiAgcmV0dXJuIGVuYzI=') )

exec (base64.b64decode ('ZGVmIGNsZWFyMyhzdHJJbnB1dCk6CiAgZW5jMj0nJwogIGlkeD0wCiAgc3RvcEF0PWxlbihzdHJJbnB1dCkKICBmb3IgeCBpbiByYW5nZSgxLHN0b3BBdCk6CiAgICBpZiAoaWR4ID49ICBzdG9wQXQpOiBicmVhawogICAgZW5jMis9KHN0cklucHV0W2lkeF0pCiAgICBmb3IgeSBpbiByYW5nZSgwLHgpOiBpZHgrPTEKCiAgZW5jMT1iYXNlNjQuYjY0ZGVjb2RlIChieXRlcyhlbmMyLCAidXRmLTgiKSApCiAgcmV0dXJuIGVuYzE=') )
