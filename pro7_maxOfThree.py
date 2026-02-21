'''def max_of_three(a, b, c):
    largest = a

    if b > largest:
        largest = b
    if c > largest:
        largest = c

    return largest


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Largest:", max_of_three(x, y, z))'''

# The following code finds the Largest of Three Numbers using nested if-else

# Taking user input
num1 = int(input("Enter a first number : "))
num2 = int(input("Enter a second number : "))
num3 = int(input("Enter a third number : "))

# Condition checking

if num1>num2:
  if num1>num3:
    print(f"First number ({num1}) is the largest.")
  else:
    print(f"Third number ({num3}) is the largest.")
else:
  if num2>num1:
    print(f"Second number ({num2}) is the largest.")
  else:
    print(f"Third number ({num3}) is the largest.")

