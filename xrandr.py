#!/usr/bin/env python
# -*- coding:utf-8 -*-
import subprocess
import argparse
import re


class ListScreen:
    def get_data(self, args :str):
        cmd = ['xrandr', args]
        proc = subprocess.Popen(lshw_cmd, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)
        self.proc =  str(proc.communicate()[0], encoding='utf-8')
        return self.proc
        
    def read_data(self, data :str):
        if len(product) == 0 :
            return ['what\'s the fuck with lshw on this hosts']
        else :
            return product

def parseARgs(parser = None ):
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increase output verbosity")
    parser.add_argument("-a", "--argv", action='append', default = [], required=False,
                        help="increase output verbosity")
    args = parser.parse_args()

    if args.verbose:
        print(f"usage is lshw.py -v | --verbose \n")
    else:
        return args
    
if __name__ == '__main__':

    screens = ListScreen()
    datas = screens.get_data()
