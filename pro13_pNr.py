def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n - 1)   # Recursive call


def permutation(n, r):
    if r > n:
        return "Invalid input (r should be <= n)"
    return factorial(n) // factorial(n - r)


n = int(input("Enter n: "))
r = int(input("Enter r: "))

print("P(n, r) =", permutation(n, r))