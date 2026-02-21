def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def permutation(n, r):
    return factorial(n) // factorial(n - r)

n = int(input("Enter n: "))
r = int(input("Enter r: "))

print("P(n,r):", permutation(n, r))

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

n = int(input("Enter n: "))
r = int(input("Enter r: "))

result = factorial(n) // factorial(n - r)

print("P(n, r) =", result)