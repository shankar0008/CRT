def count_digits(n: int) -> int:
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

if __name__ == "__main__":
    n = int(input())
    print(count_digits(n))
# Write a Python program to count the number of digits in a number. The program should take an integer input from the user and output the count of digits in that number.