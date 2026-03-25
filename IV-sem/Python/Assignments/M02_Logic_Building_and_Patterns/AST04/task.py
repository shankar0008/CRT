def right_triangle(n: int) -> str:
    result = ""
    for i in range(1, n + 1):
        result += "*" * i + "\n"
    return result.rstrip("\n")  

if __name__ == "__main__":
    n = int(input())
    print(right_triangle(n))
# Write a Python program to print a right triangle pattern of stars. The program should take an integer input from the user representing the number of rows and output the corresponding right triangle pattern.