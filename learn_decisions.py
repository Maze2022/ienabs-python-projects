import random

number = random.randint(0,10)

print(number)

if(number < 7):
    print("number is less than 7")
    
elif(number > 7):
    print("number is greater than 7")
    
else:
    print("number is 7")
    
###########################

numbers = [random.randint(0,10) for i in range(0,10)]

print(numbers)

if("7 in numbers"):
    print("7 is in")
else:
    print("7 is not in")

##################################

li_string = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
li_list = li_string.split()

#print(li_list)

def check_list_string(s, l, case_sensitive = False):
    if(not case_sensitive):
        s = s.strip().lower()
        l = [st.strip().lower() for st in l] # list comprehension
        
        # expanded list comprehension
        #new_list = []
        #for st in l:
        #    new_list.append(st.strip().lower())
        # =  new_list
    
    if(s in l):
        print(s + " is in")
    else:
        print(s + " is not in")
check_list_string("Unknown ", li_list, case_sensitive = False)

    
    
 