gen_type:str = str.lower(input("Do you wish to generate odd or even numbers? : "))
gen_amount:int = int(input("How many numbers do you wish to generate? : ")) + 1

base_value:int = int(1)

if gen_type in ["odd", "o"]:
    base_value = int(1)
    print("odd")

elif gen_type in ["even", "e"]:
    base_value = int(0)
    print("even")

elif gen_amount in ["exit"]:
    exit()

else:
    print("not valid")

output = [base_value]

for i in range(1, gen_amount):

    print(output)
    base_value += 2
    output.append(base_value)
