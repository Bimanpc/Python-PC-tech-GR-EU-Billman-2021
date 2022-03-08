a = int(input('Enter first number  : '))
b = int(input('Enter sec number : '))
c = int(input('Enter third number  : '))

largest = 0

if a > b and a > c:
    largest = a
if b > a and b > c:
    largest = b
if c > a and c > b:
    largest = c

print(largest, "the largest of three numbers.")
