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

    loop_time = timeit.timeit(stmt=loop, number=90000000)
    comprehension_time = timeit.timeit(stmt=comprehension, number=90000000)

    if comprehension_time <= loop_time:
        print("it is better to use a list comprehension")
        print(f"{comprehension_time} vs {loop_time}")
    else:
        print("it is better to use a loop")
        print(f"{loop_time} vs {comprehension_time}")

if __name__ == '__main__':
    main()