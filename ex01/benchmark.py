#!/usr/bin/env python3

import timeit

def loop(emails):
    gmails_loop = []

    for email in emails:
        if "@gmail.com" in email:
            gmails_loop.append(email)

def comprehension(emails):
    [email for email in emails]

def m(emails):
    list(map(lambda email: email if "@gmail.com" in email else None, emails))

def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
                'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
                'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
                'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
                'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']

    number_of_calls = 90000000

    loop_time = timeit.timeit(stmt=f"loop({emails})", setup="from __main__ import loop", number=number_of_calls)
    comprehension_time = timeit.timeit(stmt=f"comprehension({emails})", setup="from __main__ import comprehension", number=number_of_calls)
    map_time = timeit.timeit(stmt=f'm({emails})', setup="from __main__ import m", number=number_of_calls)

    tl = [loop_time, comprehension_time, map_time]

    tl.sort()

    tls = map(str, tl)

    if tl[0] == comprehension_time:
        print("it is better to use a list comprehension")
        print(" vs ".join(tls))
    elif tl[0] == loop_time:
        print("it is better to use a loop")
        print(" vs ".join(tls))
    elif tl[0] == map_time:
        print("it is better to use a map")
        print(" vs ".join(tls))

if __name__ == '__main__':
    main()