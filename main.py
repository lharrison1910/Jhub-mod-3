from Route import Route

while True:
    
    userInput = input("Please enter either 1, 2 or 3 for file input or STOP to end program: ")
    userInput.lower()

    match userInput:
        case "stop":
            exit()
        case "1" | "2" | "3":
            route = Route(userInput)
        case _:
            print("Error in entering, please try again")
