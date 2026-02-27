

'''3)write a python code to check whether a number is prime or not?

def is_prime(n):    
    if n <= 1:
        return False                            
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False    
    return True                 
number = int(input("Enter a number: ")) 
if is_prime(number):
    print(f"{number} is a prime number.")
else:    
    print(f"{number} is not a prime number.")       
    
'''

'''4)print the prime number with a range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Prime numbers in the range {start} to {end}:")
for num in range(start, end + 1)
'''



'''5)monotonic of a number
def is_monotonic(num):
    num_str = str(num)
    increasing = decreasing = True
    for i in range(len(num_str) - 1):
        if num_str[i] > num_str[i + 1]:
            increasing = False
        if num_str[i] < num_str[i + 1]:
            decreasing = False
    return increasing or decreasing
'''

'''6)reverse a number
def reverse_number(n):
    return int(str(n)[::-1])
number = int(input("Enter a number: "))
print(f"Reversed number: {reverse_number(number)}")
'''

