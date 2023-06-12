#!/usr/bin/python3
import sys

if __name__ == '__main__':
    ar = sys.argv
    leng_ar = len(ar)
    sum = 0

    if  leng_ar > 1:
        for k in range(1,  leng_ar):
            sum += int(ar[k])

    print(sum)
