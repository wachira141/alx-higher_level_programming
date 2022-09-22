#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    length = len(args)
    i = 1
    if length == 1:
        print("0 arguments.")
    else:
         print("{} arguments:".format(length -1))
         while i < length:
             print("{}: {}".format(i, args[i]))
             i += 1
