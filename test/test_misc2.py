#!/usr/bin/env eepython
#list deep copy
aa = [3, 2, 1]
bb = aa
#an interesting way to do deep copy
cc = aa[:]
aa.append(4)
print aa, bb, cc

#dict deep copy
