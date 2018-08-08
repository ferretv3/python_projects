#fizzbuzz!
#   For numbers 1-100, program will print 'fizz' if divisible by 3, 'buzz' if divisible
#by 5, and 'fizzbuzz' if divisible by both 3 and 5. Otherwise, the number will be printed

for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)