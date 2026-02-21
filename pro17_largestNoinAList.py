numbers = list(map(int, input("Enter numbers separated by space: ").split()))

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)

user_input = input("Enter numbers separated by space: ")

numbers = user_input.split()   # Split string into parts

largest = int(numbers[0])      # Convert first value to integer

for num in numbers:
    num = int(num)             # Convert each value to integer
    if num > largest:
        largest = num

print("Largest number:", largest)