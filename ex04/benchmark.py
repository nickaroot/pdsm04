#!/usr/bin/env python3

import timeit
import random
from collections import Counter

def my_dic(l):
    d = {}

    for k in l:
        if not (k in d):
            d[k] = 1
        else:
            d[k] += 1

    return (d)

def my_most_common(l):
    d = my_dic(l)

    s = dict(sorted(d.items(), key=lambda i: i[1], reverse=True))

    mmc = { k: s[k] for k in list(s)[:10] }

    return (mmc)

def counter_dict(l):
    c = Counter(l)
    v = dict(c)

    return (v)

def counter_most_common(l):
    c = Counter(l)
    l = c.most_common(10)

    mc = { k: v for k, v in list(l) }

    return (mc)

def main():
    l = [random.randint(1, 100) for _ in range(1000000)]

    md = my_dic(l)
    mmc = my_most_common(l)

    cd = counter_dict(l)
    cmc = counter_most_common(l)
    
    md_time = timeit.timeit(stmt=f"my_dic({l})", setup="from __main__ import my_dic")
    cd_time = timeit.timeit(stmt=f"counter_dict({l})", setup="from __main__ import counter_dict")
    mmc_time = timeit.timeit(stmt=f"my_most_common({l})", setup="from __main__ import my_most_common")
    cmc_time = timeit.timeit(stmt=f"counter_most_common({l})", setup="from __main__ import counter_most_common")

    print(f"my function: {md_time}")
    print(f"Counter: {cd_time}")
    print(f"my top: {mmc_time}")
    print(f"Counter's top: {cmc_time}")

if __name__ == '__main__':
    main()