import os

if os.access("a.txt", os.F_OK): #does file exist
    print("a.txt exists")
else:
    print("file not found, creating a.txt")
    f = open('a.txt', 'w') #creates file
    f.write("Write test from FileTest.py")
    f.close()

test = open("a.txt") #open file Test.txt

print("Reading from a.txt")
print(test.read()) #print contents of Test.txt to Console
