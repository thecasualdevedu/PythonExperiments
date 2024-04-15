name = str.capitalize(input("Input your name: "))

def nameCheck (name) :

    response = "how are you?"

    if name == "Mark" :
        response = "whats cooking!"
    
    if name == "Dude" :
        response = "killed anyone yet?"

    return response

print(str(
    "Welcome " + name + ", " + nameCheck(name)
))