#!/usr/bin/env eepython
##io.open() is an alias for the builtin open() function
#The io module provides the Python interfaces to stream handling. 
#-- Under Python 2.x, this is proposed as an alternative to the built-in file object, 
#-- but in Python 3.x it is the default interface to access files and streams.
#mode can be 
#'r'     when the file will only be read,it's default with omitted
#'w'     for only writing (an existing file with the same name will be erased)
#'a'     opens the file for appending; any data written is added to the end. 
#'+'     opens the file for both reading and writing. 
#'b'     binary mode
#        return file contents as bytes objects without any decoding
#'t'     text mode, default
#        return file as unicode strings, the bytes having been first decoded using a platform-dependent encoding or using the specified encoding if given.
#
#so the default mode is 'r+t' (open for reading text). 
#

#read() to str
import io
with io.open('/etc/nsswitch.conf', 'r') as file:
    print file; print file.read()
with open('/etc/nsswitch.conf','r') as file:
    print file; print file.read()
fo = open('/etc/nsswitch.conf','r'); print fo.read(); fo.close()
fo = open('/etc/nsswitch.conf','r'); arr = fo.readlines(); fo.close()
for i in arr: print i,

print open("/etc/nsswitch.conf").readlines()
print open("/etc/nsswitch.conf").read()
print io.open("/etc/nsswitch.conf", 'r').readlines()
print io.open("/etc/nsswitch.conf", 'r').read()
