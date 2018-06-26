S1 = "Hello World"
print("Length of the String is", len(S1))  # To find the length of a String

List1 = ["Emon", "Bakkar", "Ehassan", "Anik", "Ahad", "Sibbir"]
print("After join the list:", ", ".join(List1))  # To join the String

S2 = "Hey this is Emon"
List2 = S2.split()
print("After Split the String:{}".format(List2))  # To Split a String

S3 = "Welcome to Python Programming"
print("After replace o to e: {}".format(S3.replace("o", "e")))  # To replace any character from a string

S4 = "welcome To RPI"
print("After Capitalize the String:", S4.capitalize())  # To capitalize first letter of a String

S5 = "welcome to rpi"
print("After Upper Case:", S5.upper())  # To upper case the String

S6 = "WELCOME to RPi"
print("After lower case:", S6.lower())  # TO lower case the String

print("After swapcase the string:", S4.swapcase())  # To swap the string case

if S4.casefold() == S4.casefold():
    print("String are same")
else:
    print("String are different")  # To compare two string

print("Letter O in the string:", S3.count("o"), "Letter E in the string:", S3.count("e"))  # To count the letter
