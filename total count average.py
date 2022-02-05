#to store the numbers 
lst = [] 

#take data from the user 
while True : 
    #get input from user 
    number = input("Enter a number: ")

    #if user input is done stop the loop 
    if number == "done": 
        break 
    
    #if user enters something else than a number catch that 
    try: 
        float(number)
        lst.append(int(number))  
    except: 
        print("Invalid number")
    
#total count average 
total = 0 
count = 0 

for num in lst : 
    total += num 
    count += 1 

average = total / count 

print(total, count, average)