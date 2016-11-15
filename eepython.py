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
def handle_init(cmdline): pass
def handle_lcomment(cmdline): pass
def handle_decorator(cmdline): pass
def handle_if(cmdline): pass
def handle_block(cmdline): pass

class FSM:
    def __init__(self):
        self.startState = 'init'
        self.mstate = {
            #'state': handle_function
            'init':       handle_init, 
            'lcomment':   handle_lcomment,
            'decorator':  handle_decorator,
            'if':         handle_if,
            'block':      handle_block,
        }
    def run(self, ilist):
        pass 
