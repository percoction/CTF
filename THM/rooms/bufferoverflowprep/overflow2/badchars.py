#!/usr/bin/env python3

for x in range(0, 256):
    if x not in [0x00, 0x23, 0x3c, 0x83, 0xba]:
        print("\\x" + "{:02x}".format(x), end='')
print()
