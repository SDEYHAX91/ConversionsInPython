print("DECIMAL TO BINARY CONVERSION:\n")
n = int(input("Enter a decimal no. = "))

binary_digits = []

while n > 0:
    binary_digits.append(str(n % 2))
    n //= 2
    
binary = ''.join(reversed(binary_digits))

print("Binary representation:", binary)
