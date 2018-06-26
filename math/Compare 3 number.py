def num_com(a, b, c):
    if (a > b) and (a > c):
        return print("The First number is Biggest!!")
    elif (b > a) and (b > c):
        return print("The Second number is Biggest!!")
    elif (c > b) and (c > a):
        return print("The Third number is Biggest!!")


a = int(input("Enter First number:"))
b = int(input("Enter Second number:"))
c = int(input("Enter Third number:"))
print(num_com(a, b, c))
