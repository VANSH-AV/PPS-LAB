# Vansh Gaikwad PRN 25070521088


# Fibbonacci Sequence Using Module

def generate_fibonacci_sequence(max_value):
    fib_sequence = [0, 1]
    while True:
        next_val = fib_sequence[-1] + fib_sequence[-2]
        if next_val > max_value:
            break
        fib_sequence.append(next_val)
    return fib_sequence

