#problem1
def first_multiple(n, start):
    current = start
    while True:
        if current % n == 0:
            break
        current += 1
    return current
    
n=int(input("enter a number:"))
first_multiple(n)

#problem2
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Liftoff!")

n = int(input("Enter how many sceonds till lift off: "))
countdown(n)

#problem3
def print_triangle(height):
     for row in range(1, height + 1):
        for star in range(row):
            print("*", end=" ")
        print()
height=int(input("enter height:"))
print_triangle(height)
