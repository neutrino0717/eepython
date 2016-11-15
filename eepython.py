#!/usr/bin/env python
#########################################################################################
#
#     SCRIPT Name  :
#     PURPOSE      : get RNC status
#     Author       : Evan Liu (liuenmao@hotmail.com)
#     Website      : http://118.193.213.195
#     History      : 2016-011-15 eenmliu V.1. Created
#                  : 2016-011-xx eenmliu V.2. Xxxxxxx
#
#########################################################################################
import os
import sys
import time
import re
import glob

class EEvars:
    BLUE='\033[0;34m'
    GREEN='\033[0;32m'
    YELLOW='\033[0;33m'
    RED='\033[31m'
    ENDC='\033[0m'
    i=0
def eeprtlines(lines):
    #remove the last '\n', which is from f.readlines()
    if lines[-1] == '\n':
        lines = lines[:-1]
    if re.match('^\s*###', lines):
        print EEvars.RED + lines + EEvars.ENDC
    #if line[0:2] == "##":
    elif re.match('^\s*##', lines):
        print EEvars.YELLOW + lines + EEvars.ENDC
    elif re.match('^\s*#', lines):
        print EEvars.BLUE + lines + EEvars.ENDC
    else:
        print EEvars.GREEN + lines + EEvars.ENDC
         
   
class EEfsm:

    def eeblock_commit(self):
        eeprtlines(self.eeblock)
        exec(self.eeblock, globals())
        self.eeblock = None

    def eeblock_add(self):
        #self.eeblock = (self.eeblock == None) and self.cmdlinep or self.eeblock + '\n' + self.cmdlinep
        self.eeblock = (self.eeblock == None) and self.cmdlinep or self.eeblock + self.cmdlinep

    def eeblock_commit_add(self):
        self.eeblock_commit()
        self.eeblock_add()

    def eeblock_add_commit(self):
        self.eeblock_add()
        self.eeblock_commit()
      
    def commonhandled(self):
        if re.match(r'''[a-zA-Z0-9]*\s*=\s*['"]{3}''', self.cmdlinep): #match abc='''
            self.eestate = 'lcomment'
            self.eeblock_commit_add()
            return True
        elif re.match(r'^@', self.cmdlinep): #in decorator
            self.eestate = 'decorator'
            self.eeblock_commit_add()
            return True
        else:
            return False
        
    def prehandled(self):
        if re.match(r'(^\s*$|^#)', self.cmdlinep):    #match blank line or comment line
            self.eeblock_add()
            return True
        return False
    '''
    1. to read the first line of code
    2. end of the long comment
    '''
    def handler_init(self):
        if re.match(r'\s', self.cmdlinep):
            print "Wrong indent detected by eepython, the line is %s: %s" % (EEvars.i, cmdline)
            exit(1)
        #start with @ or long comment
        if self.commonhandled():
            return
        #match a line not start with space etc
        self.eestate = 'one'
        self.eeblock_commit_add()
    
    def handler_one(self):                ##############can we merge one and inblock???????????????????
        if re.match(r'\s', self.cmdlinep):
            self.eestate = 'inblock'
            self.eeblock_add()
            return
        #start with @ or long comment
        if self.commonhandled():        
            return
        #match a line not start with space etc
        #self.eestate = 'one'
        self.eeblock_commit_add()
    
    def handler_inblock(self):
        if re.match(r'\s', self.cmdlinep):
            self.eeblock_add()
        #start with @ or long comment
        if self.commonhandled():
            return
        #match a line not start with space etc
        self.eestate = 'one'
        self.eeblock_commit_add()
    
    def handler_lcomment(self):
        if re.match(r'''['"]{3}''', self.cmdlinep): #match ''' or """
            self.eestate = 'init'
            self.eeblock_add_commit()
        
    def handler_decorator(self):
        self.eestate = 'inblock'
        self.eeblock_add()
    
    def handler_if(cmdline): pass

    def __init__(self):
        self.eestate = 'init'
        self.eeblock = None
        self.eemstate = {
            #'state':     handler_function
            'init':       self.handler_init,      #to read the first line 
            'one' :       self.handler_one,       #after read in the first line which is not blank, not comment, not decorator, not if, while ....
            'lcomment':   self.handler_lcomment,
            'decorator':  self.handler_decorator,
            'if':         self.handler_if,
            'inblock':    self.handler_inblock,
     
        }
    def run(self, eelist):
        while EEvars.i < eelist.__len__():
            self.cmdlinep = eelist[EEvars.i]
            if not self.prehandled():
                eehandler = self.eemstate[self.eestate]
                eehandler()
            EEvars.i = EEvars.i + 1

if len(sys.argv) > 1:
    with open(sys.argv[1]) as f:
        EEfsm().run(f.readlines())
