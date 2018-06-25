S = input("Please Input Your String:")
File = open("Test.txt", "w")
File.write(S)
File.close()
File = open("Test.txt", "r")
print(File.read())
File.close()
# To read and write a text file
