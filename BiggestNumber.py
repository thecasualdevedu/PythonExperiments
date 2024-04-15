
import os

os.system("cls")

def main () :

    # setups the values
    rawValue = input("Input Value: ")
    values = list(map(int, rawValue.split( )))

    big_num = 0

    # print (values) -- used for testing the value

    # gets the values list, and cycles through it
    for value in values :
        
        # if the new value is bigger then the last set value it will update the big_num value
        if value > big_num :
            big_num = value
    
    # print results
    print (
        "The biggest number of the", len (values), "numbers is:", big_num)

main ()