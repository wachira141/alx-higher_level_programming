#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    sumnum = 0
    i = 1
    while i < length:
        sumnum += int(sys.argv[i])
        i += 1
    print(sumnum)
