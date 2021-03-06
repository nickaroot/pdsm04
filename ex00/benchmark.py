#!/usr/bin/env python3

import timeit

def loop(emails):
    gmails_loop = []

    for email in emails:
        if "@gmail.com" in email:
            gmails_loop.append(email)

def comprehension(emails):
    [email for email in emails]

def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
                'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
                'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
                'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
                'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']

    number_of_calls = 90000000

    loop_time = timeit.timeit(stmt=f"loop({emails})", setup="from __main__ import loop", number=number_of_calls)
    comprehension_time = timeit.timeit(stmt=f"comprehension({emails})", setup="from __main__ import comprehension", number=number_of_calls)

    if comprehension_time <= loop_time:
        print("it is better to use a list comprehension")
        print(f"{comprehension_time} vs {loop_time}")
    else:
        print("it is better to use a loop")
        print(f"{loop_time} vs {comprehension_time}")

if __name__ == '__main__':
    main()