#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import subprocess
import argparse
import re
import jmespath


class ListHardware:
    def get_nic_data(self):
        lshw_cmd = ['lshw', '-json']
        proc = subprocess.Popen(lshw_cmd, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)
        self.proc =  str(proc.communicate()[0], encoding='utf-8')
        return self.proc
        
    def find_class(self, data :str):
        jsonData = json.loads(data)
        bus = jmespath.search("children[?class=='bus'].children | [0]", jsonData) 
        pci = jmespath.search("@[?id=='pci'].children | [0]", bus) 
        bridge = jmespath.search("@[?class=='bridge'].children | [0]", pci) 
        multimedia = jmespath.search("@[?id=='multimedia'].children | [0]", bridge) 
        product = jmespath.search("[*].{product:product,devideid:physid} | [] ", multimedia) 
        if len(product) == 0 :
            return ['what\'s the fuck with lshw on this hosts']
        else :
            return product

def parseARgs(parser = None ):
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increase output verbosity")
    args = parser.parse_args()

    if args.verbose:
        print(f"usage is lshw.py -v | --verbose \n")
    else:
        return args
    
if __name__ == '__main__':

    list_hardware = ListHardware()
    jsonData = list_hardware.get_nic_data()
    print(list_hardware.find_class(data = jsonData))
