def fibonacci_series(n_terms):
    if n_terms <= 0:
        print("Please enter a positive integer.")
        return
    elif n_terms == 1:
        print("Fibonacci series:")
        print(0)
        return

    a, b = 0, 1
    print("Fibonacci series:")
    print(a, end=" ")
    if n_terms > 1:
        print(b, end=" ")

    for _ in range(2, n_terms):
        next_term = a + b
        print(next_term, end=" ")
        a = b
        b = next_term

    print()

try:
    num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
    fibonacci_series(num_terms)
except ValueError:
    print("Invalid input. Please enter an integer.")
