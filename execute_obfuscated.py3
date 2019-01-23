#!/usr/bin/python3
# -*- coding: utf-8 -*-

import base64
import sys

import obfuscationFunc


obfuscateMe="print ('CIAO!')"

obf=obfuscationFunc.obfuscate(obfuscateMe);
print ("Obfuscated command: "+obf)
cle=obfuscationFunc.clear(obf)
#print (cle)

exec (obfuscationFunc.clear(obf))


#exec (base64.b64decode("Zm9yIGtleSx2YWx1ZSBpbiBteURhdGEuY29weSgpLml0ZW1zKCk6CiAgaWYga2V5WzA6MV09PSdfJzogZGVsIG15RGF0YVtrZXld"))
