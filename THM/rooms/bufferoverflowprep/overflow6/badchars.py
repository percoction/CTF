#!/usr/bin/env python3

for x in range(0, 256):
    if x not in [0x00, 0x8, 0x2c, 0xad]:
        print("\\x{:02x}".format(x), end='')
print()
