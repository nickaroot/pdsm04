import timeit

def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
                'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
                'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
                'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
                'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']

    loop = f"""gmails_loop = []
for email in {emails}:
    if "@gmail.com" in email:
        gmails_loop.append(email)"""

    comprehension = f"[email for email in {emails}]"

    m = f'list(map(lambda email: email if "@gmail.com" in email else None, {emails}))'

    loop_time = timeit.timeit(stmt=loop, number=90000000)
    comprehension_time = timeit.timeit(stmt=comprehension, number=90000000)
    map_time = timeit.timeit(stmt=m, number=90000000)

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