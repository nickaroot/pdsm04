#!/usr/bin/env python3

import timeit
import sys
from functools import reduce

def loop(number_of_sum):
    sum = 0

    for i in range(1, number_of_sum + 1):
        sum += i * i

def r(number_of_sum):
    reduce(lambda x, y: x + y * y, range(1, number_of_sum + 1))

def main():
    if len(sys.argv) != 4:
        return
    
    name_of_func = sys.argv[1]
    number_of_calls = int(sys.argv[2])
    number_of_sum = int(sys.argv[3])

    func = {
        "loop": "loop",
        "reduce": "r"
    }

    if not (name_of_func in func):
        return

    func_time = timeit.timeit(stmt=f"{func[name_of_func]}({number_of_sum})", setup="from __main__ import loop, r", number=number_of_calls)

    print(func_time)

if __name__ == '__main__':
    main()