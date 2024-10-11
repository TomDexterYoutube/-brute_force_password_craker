import subprocess
import random
import string

N = 5

if str(input("use random password /")) == "y":
    password = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=N))
else:
    password = str(input("set password /"))

while True:    
    if password == input(""):
            with open("acsses.txt", "a") as file:
                file.write("sucess " + password + "\n")