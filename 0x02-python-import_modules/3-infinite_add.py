#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0

    for n in range(1, len(sys.argv)):
        sum = sum + int(sys.argv[n])

    print(sum)
