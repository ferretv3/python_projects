n_str = input("Input an integer (0 terminates): ")

n = int(n_str)
odd_sum = 0
even_sum = 0
odd_count = 0
even_count = 0
positive_int_count = 0

while n != 0:
    if n > 0:
       positive_int_count += 1
       if n % 2:
           odd_count += 1
           odd_sum = odd_sum + n
           n = int(input("Input an integer (0 terminates): "))
       else:
           even_count += 1
           even_sum = even_sum + n
           n = int(input("Input an integer (0 terminates): "))
    else:
        n = int(input("Input an integer (0 terminates): "))
        continue
    
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)
