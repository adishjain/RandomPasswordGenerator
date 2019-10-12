import random
import string

passwordLength = int(input("Pasword length:"))
print(type(passwordLength))

print("Please slect from the below options to create a password of length "+str(passwordLength))
print("A: letters only")
print("B: letters and numbers")
print("C: letters, numbers and special characters")
print("D: letters and special characters")
print("E: numbers and special characters")
print("F: numbers only")
print("G: special characters only")

methodType = input()

def randomString(methodType, num):
    string_A = string.ascii_letters
    string_B = string.ascii_letters + string.digits
    string_C = string.ascii_letters + string.digits + string.punctuation
    string_D = string.ascii_letters + string.punctuation
    string_E = string.digits + string.punctuation
    string_F = string.digits
    string_G = string.punctuation
    string_type = ""
    if methodType == "A":
        print("here")
        string_type = string_A
    elif methodType == "B":
        string_type = string_B
    elif methodType == "C":
        string_type = string_C
    elif methodType == "D":
        string_type = string_D
    elif methodType == "E":
        string_type = string_E
    elif methodType == "F":
        string_type = string_F
    else:
        string_type = string_G
    return ''.join(random.choice(string_type) for i in range(num))

methodTypeDictionary = ["A","B","C","D","E","F","G"]
if methodType in methodTypeDictionary:
    print("Password is ",randomString(methodType, passwordLength))
else:
    print("Invalid option, exiting")
