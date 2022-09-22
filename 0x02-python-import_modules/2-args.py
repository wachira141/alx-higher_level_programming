#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    length = len(args)
    i = 1
    if length <= 1:
        print("0 arguments.")
    elif length == 2:
        print("{} argument:".format(1))
        print("{}: {}".format(1, args[1]))
    else:
         print("{} arguments:".format(length -1))
         while i < length:
             print("{}: {}".format(i, args[i]))
             i += 1
