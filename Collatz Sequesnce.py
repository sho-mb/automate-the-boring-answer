def collatz(number):
    if number % 2 == 0:
        even = number // 2
        print(even)
        return even
    else:
        odd = 3 * number + 1
        print(odd)
        return odd

print("Enter number: ")
try:
    number = int(input())
except ValueError:
    print('Error: Please enter a valid integer.')

while number != 1:
    number = collatz(number)

