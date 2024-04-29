number:int = int(input("Input value: "))
num:int = 1
sum:int = 0

while num <= number:
    sum += num
    num += 1

print(f"The sum of {number} is {sum}")