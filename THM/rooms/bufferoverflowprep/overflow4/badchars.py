#!/usr/bin/env python3

for x in range(0, 256):
    if x not in [0x00, 0xa9, 0xcd, 0xd4]:
        print("\\x" + "{:02x}".format(x), end='')
print()
