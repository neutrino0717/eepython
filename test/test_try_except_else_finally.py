#!/usr/bin/env eepython
x = 5
y = 0
try:
    result = x / y
except ZeroDivisionError:
    print "division by zero!"
else:
    print "result is", result
finally:
    print "executing finally clause"
