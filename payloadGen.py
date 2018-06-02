#!/usr/bin/python

import os
import sys
from binascii import unhexlify
from binascii import hexlify

def main():
    argc = len(sys.argv)

    if (argc == 1):
        print "Usage: "
        print "./payloadGen.py [payloadLen] [payloadVal] [outfile]"
        print "ex) ./payloadGen.py 40 0x61626364"

    padding = 'A' * int(sys.argv[1])

    if (argc < 3):
        print padding
        return

    payloads = sys.argv[2].split(',')

    finalPayload = ""
    if (argc < 4):
        for payload in payloads:
            reversedPayload = unhexlify(payload)[::-1]
            print reversedPayload
            finalPayload += reversedPayload

        print type(finalPayload)

    else:
        outfileName = sys.argv[3]
        with open(outfileName, 'wb') as outfile:
            outfile.write(padding)
            for payload in payloads:
                reversedPayload = unhexlify(payload)[::-1]
                outfile.write(reversedPayload)

if __name__ == '__main__':
    main()
