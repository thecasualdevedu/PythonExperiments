age = int(input("What is your age: "))

if age < 13 :
    print("User is not allowed.")
    exit

elif age < 18 :
    print("User restricted.")
    exit
    
elif age > 18 :
    print("User has full access")
    exit
