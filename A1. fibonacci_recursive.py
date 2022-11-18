def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


n_terms = int(input("Enter number of terms"))
for i in range(n_terms):
    print(fib(i))
