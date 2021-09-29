import random

# Inputs lenght of password
passlen = int(input("Enter the length of password: "))

# All charecters considered in password creation
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# Generating random password and printing
p =  "".join(random.sample(s,passlen ))
print ("The suggested password is: " , p)
