print("--------------------------------Welcome to the fizzbuzz game!----------------------------------------")

num = int(input("Please write a number between 1 and 100: "))

for num in range(1, num):
    if num % 15 is 0:
        print("FizzBuzz")
    elif num % 3 is 0:
        print("Fizz")
    elif num % 5 is 0:
        print("Buzz")
    else:
        print(num)
