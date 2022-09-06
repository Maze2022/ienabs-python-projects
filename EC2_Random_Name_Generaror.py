#EC2 Random Name Generator

import random #defines a series of functions for generating random integers
import string #string is a built-in function but importing it allows access to some useful constants

# 1) Prompt users to input the number of instances

ec2_inst = int(input("How many instances would unique EC2 names be assigned to? "))

# 2) Prompt user to input department requesting for instances

auth_dept = ["FinOps", "Accounting", "Marketing"]

dept = input("Please select department making the request:\n")

if dept in auth_dept:
    print("Request approved")
else:
    print("Not authorized to use name generator, select from authorized departments")
    exit()

# 3) Generate random characters and numbers and assign to unique ec2 named variable

ec2_rand_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))

# 4) Assign variable to represent unique ec2 name

unique_ec2_name = (dept + '-' + ec2_rand_chars)

print(unique_ec2_name)

print("Your request has been completed! Thank you")
