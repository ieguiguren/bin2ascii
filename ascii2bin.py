#!/usr/bin/env python

import binascii

while True:
    msg = raw_input('Message: ')
    chain = str(bin(int(binascii.hexlify(msg),16)))
    print chain[2::]
