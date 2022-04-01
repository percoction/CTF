#!/usr/bin/env python3

for x in range(0, 256):
    if x not in [0x00, 0x7, 0x8, 0x2e, 0x2f, 0xa0, 0xa1]:
        print("\\x" + "{:02x}".format(x), end='')
print()
