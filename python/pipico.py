def fibonacci(n):
    # Check if the input is a positive integer
    if n <= 0:
        print("Input should be a positive integer.")
        return

    # Initialize the first two numbers of the Fibonacci sequence
    fib_seq = [0, 1]

    # Calculate the Fibonacci sequence
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    return fib_seq


# Test the code
num_terms = int(input("Enter the number of terms: "))
fibonacci_seq = fibonacci(num_terms)
print("Fibonacci Sequence:", fibonacci_seq)
