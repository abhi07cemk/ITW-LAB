numbers = list(map(int, input("Enter numbers separated by space: ").split()))

minimum = numbers[0]
maximum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print("Minimum:", minimum)
print("Maximum:", maximum)