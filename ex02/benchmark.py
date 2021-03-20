#!/usr/bin/env python3

import timeit
import sys

def loop(emails):
    gmails_loop = []

    for email in emails:
        if "@gmail.com" in email:
            gmails_loop.append(email)

def comprehension(emails):
    [email for email in emails]

def m(emails):
    list(map(lambda email: email if "@gmail.com" in email else None, emails))

def f(emails):
    list(filter(lambda email: "@gmail.com" in email, emails))

def main():
    if len(sys.argv) != 3:
        return
    
    name_of_func = sys.argv[1]
    number_of_calls = int(sys.argv[2])

    func = {
        "loop": "loop",
        "list_comprehension": "comprehension",
        "map": "m",
        "filter": "f"
    }

    if not (name_of_func in func):
        return

    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
                'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
                'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
                'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
                'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']

    func_time = timeit.timeit(stmt=f"{func[name_of_func]}({emails})", setup="from __main__ import loop, comprehension, m, f", number=number_of_calls)

    print(func_time)

if __name__ == '__main__':
    main()