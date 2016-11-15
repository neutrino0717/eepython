#!/usr/bin/env eepython

#make dict with two list
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dd = dict(zip(keys, values))
print dd

#reverse dict
print {v: k for k, v in dd.items()}

#reverse dict
print                 dd.items()
print            zip(*dd.items())
print            zip(*dd.items())[::-1]
print      zip(*(zip(*dd.items())[::-1]))
print dict(zip(*(zip(*dd.items())[::-1])))

#reverse dict
print dict(zip(dd.values(), dd.keys()))
