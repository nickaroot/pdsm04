#!/usr/bin/env python3

import timeit
import sys
from functools import reduce

def main():
    if len(sys.argv) != 4:
        return
    
    name_of_func = sys.argv[1]
    number_of_calls = int(sys.argv[2])
    number_of_sum = int(sys.argv[3])

    print(name_of_func, number_of_calls, number_of_sum)

if __name__ == '__main__':
    main()