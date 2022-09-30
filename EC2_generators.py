#EC2 Random Name Generator

# Create unique EC2 names that the users can attach to the instances. 
# 1 Users should input how many EC2 instances they want names for and output the same amount of unique names.
# 2 Users should input the name of their department that is used in the unique name
# 3 Generate random characters and numbers that will be included in the unique name

# Week 13 EC2 Random Name Generator Project 

#!/usr/bin/env python3.7

import random 
import string 

# Allow the user to input how many EC2 instances they want names for and output the same amount of unique names.
ec2_count = input( 'Enter the number of EC2 instances\n')

# Allow the user to input the name of their department that is used in the unique name 
depts = input('Enter in what department you are in\n')

# Generate random characters and numbers that will be included in the unique name.
for _ in range (int(ec2_count)):
    print (str(depts), ''.join([choice(string.ascii_uppercase + string.digits) for _ in range(N)]))






