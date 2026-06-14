#problem1
def sum_to_n(n):
    total = 0  

    for i in range(1, n + 1):
        total =total+ i

    print(total)
n=int(input("Enter number:"))
sum_to_n(n)

#problem2
def times_table(n):
    for i in range (1,11):
        print(f"{n} x {i} = {n * i}")
n=int(input("enter the number"))
times_table(n)

#problem3
def class_g(score):
    if score <0 or score >100:
        return"invalid score"
    elif score >=90:
        return"A"
    elif score >=80 and 89:
        return"B"
    elif score >=70 and 79:
        return"C"
    elif score >=60 and 69:
        return"D"
    elif score >59:
        return"F"
score=int(input("enter score:"))
class_g(score)

#problem4
def is_leap_year(year):
    if year%4==0 and year%100!=0:
        print("true")
    else:
        print("false")
year=int(input("enter a year"))
is_leap_year(year)
