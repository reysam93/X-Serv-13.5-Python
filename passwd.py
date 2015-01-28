#!/usr/bin/python
# -*- coding: utf-8 -*-

fich = open("/etc/passwd", "r")
maquinas = fich.readlines()
dicc = {}

for maquina in maquinas:
    user = maquina.split(":")[0]  
    shell = maquina.split(":")[-1]
    dicc[user] = shell

print len(maquinas), "users"
print "user: root    shell:", dicc["root"],

try:
    print "user: imaginario    shell:", dicc["imaginario"],
except KeyError:
    print "WRONG USER NAME" 
