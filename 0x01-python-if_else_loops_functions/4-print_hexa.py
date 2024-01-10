#!/usr/bi/python3
for i in range(0, 99):
    if(i > 9 and i <= 15):
        if i == 10:
            print(i, " = 0x", "a")
        elif i == 11:
            print(i, " = 0x", "b")
        elif i == 12:
            print(i, " = 0x", "c")
        elif i == 13:
            print(i, " = 0x", "d")
        elif i == 14:
            print(i, " = 0x", "e")
        elif i == 15:
            print(i, " = 0x", "f")
    else:
        print(i, " = 0x", i)
