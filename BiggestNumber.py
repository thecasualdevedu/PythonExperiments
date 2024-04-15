
import os

os.system("cls")

def main () :

    rawValue = input("Input Value: ")
    values = list(map(int, rawValue.split( )))

    big_num = 0

    # print (values) -- used for testing the value

    for value in values :

        if value > big_num :
            big_num = value
    
    print (
        "The biggest number of the", len (values), "numbers is:", big_num)

main ()