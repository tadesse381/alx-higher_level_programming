#!/usr/bin/python3
import sys

if __name__ == '__main__':
    """
Print the argument list 

    """
    ar = sys.argv
    leng_ar = len(ar) - 1

    if  leng_ar > 1:
        print(leng_ar, 'arguments:')
        for j in range(1,  leng_ar + 1):
            print('{:d}: {}'.format(j, ar[j]))
    elif  leng_ar == 1:
        print(leng_ar, 'argument:')
        for k in range(1,  leng_ar + 1):
            print('{:d}: {}'.format(k, ar[k]))
    elif  leng_ar == 0:
        print(leng_ar, 'arguments.')
