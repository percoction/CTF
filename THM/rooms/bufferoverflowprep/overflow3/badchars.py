#!/usr/bin/python3

for x in range(0, 256):
    if x not in [0x00, 0x01, 0x11, 0x40, 0x5f, 0xb8, 0xee]:
        print("\\x" + "{:02x}".format(x), end='')
print()
