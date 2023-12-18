#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import subprocess
import argparse


class ListHardware:
    def get_nic_data(self, className :str):
        lshw_cmd = ['lshw', '-json', '-c', className]
        proc = subprocess.Popen(lshw_cmd, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)
        self.proc = proc.communicate()[0]

    def read_data(self):
        self.result= []
        tmp = {}
        for entry in json.loads(self.proc) :
            if 'vendor' in entry :
                tmp['vendor'] = entry['vendor']
                tmp['product'] = entry['product']
                self.result.append(tmp)
        return self.result

def parseARgs(parser = None ):
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increase output verbosity")
    parser.add_argument("-c", "--className", action="store", default = 'display',
                    help="classe utilisée pour lshw")
    args = parser.parse_args()

    if args.verbose:
        print(f"usage is lshw.py -v | --verbose \n")
    else:
        return args
    
options = parseARgs(argparse.ArgumentParser(description='lance lshw en mode python et retorun un nested listant les cartes Vidéos'))
if __name__ == '__main__':

    list_hardware = ListHardware()
    list_hardware.get_nic_data(className=options.className)
    result = list_hardware.read_data()
    print(result)
