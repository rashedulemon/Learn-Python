import math


def triangle_area(a, b, c):
    if (a + b) > c and (b + c) > a and (a + c) > b:
        s = (a + b + c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        return print("The area is:", area)
    else:
        return print("Triangle is not possible.")


a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))
print(triangle_area(a, b, c))
