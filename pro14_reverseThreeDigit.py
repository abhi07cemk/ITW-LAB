num = int(input("Enter three-digit number: "))

reverse = (num % 10) * 100 + ((num // 10) % 10) * 10 + (num // 100)

print("Reversed number:", reverse)