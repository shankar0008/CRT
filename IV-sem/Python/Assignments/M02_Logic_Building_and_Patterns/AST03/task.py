def sum_of_digits(n: int) -> int:
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

if __name__ == "__main__":
    n = int(input())
    print(sum_of_digits(n))
# Write a Python program to calculate the sum of digits of a number. The program should take an integer input from the user and output the sum of its digits.