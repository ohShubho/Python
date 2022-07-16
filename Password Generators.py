import random 

chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"

while 1: 
    password_len = int(input("Enter the length of the password: "))
    password_count = int(input("Enter the number of passwords to generate: "))
    for i in range(password_count):
        password = ""
        for j in range(password_len):
            password += random.choice(chars)
        print(password)