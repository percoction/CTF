#!/usr/bin/env python3

for x in range(0, 256):
    if x not in [0x00, 0x16, 0x2f, 0xf4, 0xfd]:
        print("\\x" + "{:02x}".format(x), end='')
print()
