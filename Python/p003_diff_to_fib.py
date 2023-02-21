def diff_to_fib(num):
    values = [0, 1]

    while True:
        current_fib = sum(values[-2:])
        if current_fib >= num:
            return current_fib - num

        values.append(current_fib)
