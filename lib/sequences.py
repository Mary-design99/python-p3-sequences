def print_fibonacci(length):
    fib_sequence = []

    if length <= 0:
        pass # fib_sequence is already an empty list
    elif length == 1:
        fib_sequence.append(0)
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < length:
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_fib)
    
    # This line now executes for all cases, including length <= 0
    print(fib_sequence)
    return fib_sequence