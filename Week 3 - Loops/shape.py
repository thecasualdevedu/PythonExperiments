char:str = "•"

def triangle(size:int):

    for i in range(1, size):
        print(f" {char}"*i)

def square(size:int):

    for i in range(1, size):
        print(f" {char}"* size)

shape = str.lower(input("Select shape | Square) Triangle) : "))
size = int(input("Select size : "))
char = str(input("Select char : ")) or str("•")


if shape == "s" or shape == "square":
    square(size)

elif shape == "t" or shape == "triangle":
    triangle(size)

else:
    print(f"{shape} not valid")
    exit()