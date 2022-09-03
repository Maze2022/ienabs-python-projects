import random

numbers = []

for i in range(0,100):
  numbers.append(random.randint(0,10))
  
for i in range(0,100):
     if(random.randint(0,10) == 7):
         print("seven")
         break
print(i)

############################

number = random.randint(0,10)
counter = 0

while(number != 7):
    number = random.randint(0,10)
    counter += 1

print(counter)