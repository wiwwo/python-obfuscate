#!/usr/bin/python3
# -*- coding: utf-8 -*-

import base64
import sys

import obfuscationFunc


obfuscateMe="print ('CIAO!')"

print ("\nClear command: "+obfuscateMe)
print  ("Base64 command: "+str(base64.b64encode (bytes(obfuscateMe, "utf-8") )))

obf=obfuscationFunc.obfuscate(obfuscateMe);
print ("\nobfuscate\nObfuscated command: "+obf)
cle=obfuscationFunc.clear(obf)

print ("Executing:")
exec (obfuscationFunc.clear(obf))

print ("---------------------------------------------------------")

obf=obfuscationFunc.obfuscate2(obfuscateMe);
print ("obfuscate2\nObfuscated command: "+obf)
cle=obfuscationFunc.clear2(obf)

print ("Executing:")
exec (obfuscationFunc.clear2(obf))

print ("---------------------------------------------------------")

obf=obfuscationFunc.obfuscate3(obfuscateMe);
print ("obfuscate3\nObfuscated command: "+obf)
cle=obfuscationFunc.clear3(obf)

print ("Executing:")
exec (obfuscationFunc.clear3(obf))
