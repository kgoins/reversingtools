#!/usr/bin/python

import os
import sys

import argparse

from binascii import unhexlify
from binascii import hexlify


parser = argparse.ArgumentParser()
parser.add_argument('-l', '--paddinglen', help="Number of padding chars before payload")
parser.add_argument('-p', '--payload', help="Payload in hex")
parser.add_argument('-o', '--outfile', help="Output file")

def convertPayload(payload):
    if (payload.startswith("0x")):
        payload = payload.strip("0x")

    reversedPayload = unhexlify(payload)[::-1]
    return reversedPayload

def main():
    args = parser.parse_args()

    padding = ""
    if (args.paddinglen):
        padding = 'A' * int(args.paddinglen)

    if (args.payload):
        payload = convertPayload(args.payload)
    else:
        payload = ""
        
    if (args.outfile):
        with open(args.outfile, 'wb') as outfile:
            outfile.write(padding)
            outfile.write(payload)
    else:
        print padding + payload

if __name__ == '__main__':
    main()
